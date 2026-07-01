#!/usr/bin/env python3

import argparse
import json
import os
from typing import Dict

from jinja2 import Environment
from jinja2.loaders import FileSystemLoader

def main() -> int:
    parser = argparse.ArgumentParser(
        prog="AMS swagger parser",
        description="Extracts AMS configuration data",
    )
    parser.add_argument(
        "-i",
        "--input-file",
        dest="swagger_path",
        required=False,
        help="Path to the swagger json file (Should conform to swagger spec 2.0)",
    )
    parser.add_argument(
        "-o",
        "--output",
        dest="output_file",
        help="Destination of the rendered configuration file",
        default="reference/ams-configuration.md",
    )
    args = parser.parse_args()
    with open(args.swagger_path, mode="r") as f:
        swagger = json.load(f)
    parse_swagger(swagger, args.output_file)


def insert_custom_fields(props: Dict):
    for prop in props.values():
        val = prop.pop("x-docs-ref", "")
        if val:
            prop["x_docs_ref"] = val
        val = prop.pop("x-deprecated-since", "")
        if val:
            prop["x_deprecated_since"] = val


def parse_swagger(swagger, output_file):
    configs = _parse_config_schema(swagger)
    nodes = _parse_node_schema(swagger)
    insert_custom_fields(configs)
    insert_custom_fields(nodes)
    env = Environment(loader=FileSystemLoader("."))
    templ = env.get_template("scripts/ams-configuration.md.j2")
    text = templ.render(configs=configs, nodes=nodes)

    # Write the output file only if the new text is different from
    # the existing text. This function is called during the Sphinx
    # build and writing it unconditionally causes Sphinx to treat
    # the generated output file as modified and trigger another build,
    # thereby causing an infinite loop.
    existing_text = ""
    if os.path.exists(output_file):
        with open(output_file) as op:
            existing_text = op.read()
    if text != existing_text:
        with open(output_file, mode="w+") as op:
            op.write(text)


def _parse_config_schema(swagger) -> dict:
    ams_config_path = "/1.0/config"
    config_props = swagger["paths"][ams_config_path]["get"]["responses"]["200"][
        "schema"
    ]["properties"]["metadata"]["properties"]["config"]["properties"]
    for prop in config_props.values():
        if "description" in prop:
            prop["description"] = prop["description"].replace("\n", " ")
    return config_props


def _parse_node_schema(swagger) -> dict:
    node_props = swagger["definitions"]["NodePatch"]["properties"]
    for base, prop in dict(node_props).items():
        key = ""
        if prop["type"] == "object":
            key = "additionalProperties"
        if prop["type"] == "array":
            key = "items"
        if key:
            if schema_name := prop[key].get("$ref"):
                name = schema_name.split("/")[-1]
                if schema := swagger["definitions"][name]:
                    for subprop_name, subprop_attrs in schema["properties"].items():
                        if subprop_name == "id":
                            continue
                        new_base = base
                        if base == "gpus":
                            new_base = f"{base}.<id>"
                        node_props[f"{new_base}.{subprop_name.replace('_', '-')}"] = (
                            subprop_attrs
                        )
            node_props.pop(base)
        else:
            val = node_props.pop(base)
            node_props[base.replace("_", "-")] = val
        if "description" in prop:
            prop["description"] = prop["description"].replace("\n", " ")
    return node_props


if __name__ == "__main__":
    SystemExit(main())
