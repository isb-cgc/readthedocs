'''
copyright 2017, Institute for Systems Biology.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import requests
import json
import os

JSON_FILE_DIRECTORY = 'endpoints_json_files_v3'
JS_SPACE = '  '

def set_endpoint_info(endpoint):
    global RESP_JSON, BASE_URL, DEV_DOCUMENTATION_DIRECTORY_PATH
    DEV_DOCUMENTATION_DIRECTORY_PATH = 'docs/source/sections/progapi/progapi3_{}/'.format(endpoint.split('_')[2])
    if not os.path.isdir(DEV_DOCUMENTATION_DIRECTORY_PATH):
        os.makedirs(DEV_DOCUMENTATION_DIRECTORY_PATH)
    if not os.path.isdir(JSON_FILE_DIRECTORY):
        os.makedirs(JSON_FILE_DIRECTORY)
    try:
        resp = requests.get('https://mvm-api-dot-isb-cgc.appspot.com/_ah/api/discovery/v1/apis/{}/v3/rest'.format(endpoint))
        RESP_JSON = resp.json()
        BASE_URL = RESP_JSON['baseUrl']
    except:
        with open(JSON_FILE_DIRECTORY + '/resp_json_v3.json', 'r') as f:
            contents = f.read()
        RESP_JSON = json.loads(contents)
        BASE_URL = RESP_JSON['baseUrl']

def get_methods_list():
    '''
    returns list of keys from methods object in RESP_JSON
    '''
    methods_list = []
    for method in RESP_JSON['resources']['cohort_endpoints']['resources']['cohorts']['methods'].keys():
        methods_list.append(method)
    return methods_list

def get_methods_pathnames_list():
    get_methods_pathnames_list = []
    for method in RESP_JSON['resources']['cohort_endpoints']['resources']['cohorts']['methods'].values():
        get_methods_pathnames_list.append(method['path'])
    return get_methods_pathnames_list

def get_csv_table_heading(headers=None, widths=None):
    # todo: change this so headers default is ["**Parameter name**", "**Value**", "**Description**"]
    # todo: make widths default [50, 10, 50]
    header_string = '.. csv-table::\n'
    if headers is None:
        header_string += '\t:header: "**Parameter name**", "**Value**", "**Description**"\n'
    if widths is None:
        header_string += '\t:widths: 50, 10, 50\n'
    return header_string

def get_next_parameter_javascript_row(message_class_name, started_string, level=0, resource_name=None, method_name=None):
    '''
    Recursive function returning javascript formatting of restructured text.
    level will indicate number of JS_SPACE spaces
    todo: figure out tab spaces w nested objects vs lists of nested objects
    '''
    message_class_properties = RESP_JSON['schemas'][message_class_name]['properties']
    sorted_message_class_properties = list(sorted(message_class_properties.iteritems(),
                                                  key=lambda s: s[0].lower()))
    # print message_class_name + ": level " + str(level)
    for key, val in sorted_message_class_properties:
        # print key + ": level " + str(level)
        # possibilities
        # 1. value is a 'number' or 'string'
        if val.get('type') is not None and val.get('type') != 'array':  # todo: if val['type'] is string but val.get('format') is int64, could clarify that it is a digit optionally in the form of a string?
            started_string += (level+2)*JS_SPACE + '"{}": {}'.format(key, val.get('type'))
        # 2. value is a nested object message class
        if val.get('type') is None:
            started_string += (level+2)*JS_SPACE + '"' + key + '": {\n'
            next_message_class = val['$ref']
            level += 1
            started_string = get_next_parameter_javascript_row(next_message_class,
                                                               started_string,
                                                               level=level,
                                                               resource_name=resource_name,
                                                               method_name=method_name)
            level -= 1
        # 3. value is a list of either...
        if val.get('type') == 'array':
            # 3. a) i.e. this is a list of strings or numbers
            if val['items'].get('type') is not None:  # assuming no lists of lists so don't check for is not 'array'
                started_string += (level+2)*JS_SPACE + '"{}": [{}]'.format(key, val['items'].get('type'))
            # 3. b) value is a list of (nested?) object message classes
            else:
                started_string += (level+2)*JS_SPACE + '"{}": [\n'.format(key)
                level += 1
                started_string += + (level+2)*JS_SPACE + '{\n'
                next_message_class = val['items'].get('$ref')
                level += 1
                started_string = get_next_parameter_javascript_row(next_message_class,
                                                                   started_string,
                                                                   level=level,
                                                                   resource_name=resource_name,
                                                                   method_name=method_name)
                level -= 2
                started_string += '\n' + (level+2)*JS_SPACE + ']'
        # end possibilities
        # check if we are at the end of the message_class_properties
        current_index = sorted_message_class_properties.index((key, val))
        end_index = len(sorted_message_class_properties) - 1
        # if we are at the end
        if current_index == end_index:
            started_string += '\n'
            level -= 1
        # if we are not at the end, add a comma
        else:
            started_string += ",\n"
    started_string += (level+2)*JS_SPACE + '}'
    return started_string

def get_next_property_table_row(message_class_name, started_string, level='', resource_name=None, method_name=None):
    '''
    change name to get next response table row?
    Recursive function returning csv formatting of restructured text.
    level indicates number of dots
    '''
    message_class_properties = RESP_JSON['schemas'][message_class_name]['properties']
    sorted_message_class_properties = list(sorted(message_class_properties.iteritems(),
                                                  key=lambda s: s[0].lower()))

    description_filename = message_class_name + '.json'
    with open(JSON_FILE_DIRECTORY + '/' + description_filename, 'r+') as f:
        description_contents = f.read()
        description_json = json.loads(description_contents)
        if message_class_name == 'Api3CohortGetListHelperCohortDetails' and method_name == 'list':
            description_json.pop('samples')
            description_json.pop('cases')

    for key, val in sorted_message_class_properties:
        if message_class_name == 'Api3CohortGetListHelperCohortDetails' and method_name == 'list' and key in ('cases', 'samples'):
            continue
        
        # possibilities
        # 1. value is a number or string
        if val.get('type') is not None and val.get('type') != 'array':
            started_string += '\t{level}{key}, {type}, "{desc}"\n'\
                .format(level=level,
                        key=key,
                        type=val.get('type'),
                        desc=description_json[key])
        # 2. value is a nested object message class
        if val.get('type') is None:
            started_string += '\t{level}{key}, nested object, "{desc}"\n'\
                .format(level=level, key=key, desc=description_json[key])
            level += key + '.'  # will this work?
            next_message_class = val['$ref']
            started_string = get_next_property_table_row(next_message_class,
                                                         started_string,
                                                         level=level,
                                                         resource_name=resource_name,
                                                         method_name=method_name)
            # go up one level i.e. truncate at next to last dot
            level = level[:level[:level.rfind('.')].rfind('.')+1]
        # 3. value is a list of either...
        if val.get('type') == 'array':
            started_string += '\t{level}{key}[], list, "{desc}"\n'.format(level=level, key=key, desc=description_json[key])
            # 3. a) i.e. this is a list of strings or numbers
            if val['items'].get('type') is not None:  # assuming no lists of lists so don't check for is not 'array'
                pass
            # 3. b) value is a list of nested object message classes
            else:
                level += key + '[].'
                next_message_class = val['items'].get('$ref')
                started_string = get_next_property_table_row(next_message_class,
                                                             started_string,
                                                             level=level,
                                                             resource_name=resource_name,
                                                             method_name=method_name)
                # go up one level i.e. truncate at next to last dot
                level = level[:level[:level.rfind('.')].rfind('.')+1]
    return started_string
def create_new_rst_file(method_name):
    '''
    creates an rst file with the name of the endpoint method
    in the folder docs/sections/progapi/progapi2
    '''
    file_name = method_name + ".rst"
    file_path = str(DEV_DOCUMENTATION_DIRECTORY_PATH + file_name)
    f = open(file_path, 'w')
    f.close()

def get_json_file_contents(file_name):
    with open(JSON_FILE_DIRECTORY + '/' + file_name + '.json', 'r') as f:
        contents = f.read()
    return json.loads(contents)

def write_rst_file_header(resource, method, endpoint, program):
    '''
    write the title heading,
     description
     example from command line
     example from API explorer
     access control
     request (GET or POST) and the full url
    '''
    method_json = RESP_JSON['resources'][resource]['methods'][method]
    method_path_name = method_json['path']
    description = method_json['description']
    http_method = method_json['httpMethod']
    file_name = resource + '_' + method
    example_contents_json = get_json_file_contents('examples{}_v3'.format(program.lower()))
    api_explorer_example_contents_json = get_json_file_contents('api_explorer_examples{}_v3'.format(program.lower()))
    python_example_contents_json = get_json_file_contents('python_examples{}_v3'.format(program.lower()))
    example_text = ''
    if example_contents_json.get(file_name):
        example_text = '\n\n**Example**::\n\n\t' + example_contents_json[file_name] % (endpoint)
    api_explorer_example_text = ''
    if example_contents_json.get(file_name):
        api_explorer_example_text = "\n\n**API explorer example**:\n\nClick `here <{}/>`_ " \
                                    "to see this endpoint in Google's API explorer.".format(
            api_explorer_example_contents_json[file_name].format(endpoint))
    python_example_text = ''
    if python_example_contents_json.get(file_name):
        python_example_text += '\n\n**Python API Client Example**::\n\n'
        if (resource == 'cohorts' and method != 'preview') or resource == 'users':  # authentication required
            python_example_text += python_example_contents_json['authorized_imports'] + '\n\n' \
                                   + python_example_contents_json['auth_globals'] + '\n\n' \
                                   + python_example_contents_json['get_credentials'] + '\n\n' \
                                   + python_example_contents_json['get_authorized_service'].format(endpoint) + '\n\n'
        else:
            python_example_text += python_example_contents_json['unauthorized_imports'] + '\n\n' \
                                   + python_example_contents_json['get_unauthorized_service'].format(endpoint) + '\n\n'
        try:
            if "'{0}'" in python_example_contents_json[file_name]:
                python_example_text += python_example_contents_json[file_name].format(endpoint)
            else:
                python_example_text += python_example_contents_json[file_name]
        except Exception as e:
            raise
    # print python_example_text
    # write title, e.g.
    # cohorts().create()
    # ################################
    header_text = "{resource}().{method}()\n{underscore}\n".format(
        resource=resource,
        method=method,
        underscore='#'*len(resource + '.()' + method + '.()'))
    # write description, e.g.
    # Takes a cohort id as a required parameter and returns cloud storage paths to files associated with all the samples in that cohort, up to a default limit of 10,000 files. Authentication is required. User must have READER or OWNER permissions on the cohort.
    header_text += description
    # write example, e.g.
    # $ python isb_curl.py "https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/datafilenamekey_list_from_cohort?cohort_id={YOUR_COHORT_ID}"
    header_text += example_text
    # write api explorer example
    header_text += api_explorer_example_text
    # write python example
    header_text += python_example_text + '\n'
    # write http request, e.g.
    # GET https://api-dot-isb-cgc.appspot.com/_ah/api/cohort_api/v1/datafilenamekey_list_from_cohort
    header_text += "\n\n**Request**\n\nHTTP request::\n\n\t{http_method} {base_url}{method_path_name}\n\n".format(
        method_path_name=method_path_name,
        http_method=http_method,
        base_url=BASE_URL)
    with open(DEV_DOCUMENTATION_DIRECTORY_PATH + file_name + '.rst', 'w+') as f:
        f.write(header_text)

def get_next_parameter_table_row(parameter_json, allowed_values={}, method_name=None, request_body=False):
    '''
    No need for this to be a recursive function since request parameters
    are only a list. Takes a json object of parameters and returns a string
    for a csv-formatted rst table.
    '''
    sorted_parameter_json = list(sorted(parameter_json.iteritems(), key=lambda s: s[0].lower()))
    return_string = ''
    for key, val in sorted_parameter_json:
        value_entry = 'list' if val.get('type') == 'array' else val.get('type')
        description = "Required. " if val.get('required') else 'Optional. '
        # if val.get('format') and val.get('format').startswith('int'):
        #     value_entry = 'integer'
        try:
            if allowed_values.get(key):
                description += "Possible values include: '" + "', '".join(allowed_values.get(key)) + "'."
        except TypeError, e:
            description += "Possible values include: "
            description += json.dumps(allowed_values.get(key)).strip('[').strip(']') + "."
        return_string += '\t{}{},{},"{}"\n'.format(key,
                                                 '[]' if value_entry == 'list' else '',
                                                 value_entry,
                                                 description)
    return return_string

def write_rst_file_path_parameters(resource, method):
    '''
    rst table from csv table of path parameters
    '''
    method_json = RESP_JSON['resources'][resource]['methods'][method]
    file_name = resource + '_' + method + '.rst'
    method_parameters = method_json.get('parameters')
    if method_parameters is None:
        parameter_text = """**Parameters**\n\nNone\n\n"""
    else:
        csv_table_heading = get_csv_table_heading()
        csv_table_body = get_next_parameter_table_row(method_parameters)
        parameter_text = """**Parameters**\n\n{csv_header}\n{csv_table_body}\n\n"""\
            .format(csv_header=csv_table_heading,
                   csv_table_body=csv_table_body)

    # todo: f.read(), then f.seek() to find "Parameters" and replace text
    # from just the parameters section
    with open(DEV_DOCUMENTATION_DIRECTORY_PATH + file_name, 'a+') as f:
        f.write(parameter_text)

def write_rst_file_request_body(resource, method, program):
    '''
    write javascript code block of request body parameters
    and rst table from csv table of request body parameters
    '''
    method_json = RESP_JSON['resources'][resource]['methods'][method]
    file_name = resource + '_' + method + '.rst'
    method_request = method_json.get('request')
    if method_request is None:
        return
    request_body_message_class_name = method_request['$ref']  # e.g. "ApiIsbCgcApiIsbCgcApiHelpersMetadataRangesItem"
    request_desc = 'In the request body, supply a metadata resource with the following properties:'
    js_block_header = '.. code-block:: javascript\n\n'
    js_block_body = get_next_parameter_javascript_row(request_body_message_class_name,
                                                      JS_SPACE + '{\n')
    message_class_properties = RESP_JSON['schemas'][request_body_message_class_name]['properties']
    csv_header = get_csv_table_heading()
    allowed_values = {}
    if method in ['preview', 'create'] and resource == 'cohorts':
        with open(JSON_FILE_DIRECTORY + '/allowed_values_v3%s.json' % program, 'r') as f:
            contents = f.read()
        allowed_values = json.loads(contents)
    csv_body = get_next_parameter_table_row(message_class_properties,
                                            method_name=method,
                                            request_body=True,
                                            allowed_values=allowed_values)
    request_body_text = "Request body\n\n{}\n\n{}{}\n\n{}\n{}\n\n"\
        .format(request_desc, js_block_header, js_block_body, csv_header, csv_body)
    with open(DEV_DOCUMENTATION_DIRECTORY_PATH + file_name, 'a+') as f:
        f.write(request_body_text)

def write_rst_file_response_section(resource, method):
    '''
    write javascript code block of response body properties
    and rst table from csv table of response body properties
    '''
    method_json = RESP_JSON['resources'][resource]['methods'][method]
    file_name = resource + '_' + method + '.rst'
    method_response = method_json.get('response')
    if method_response is None:
        response_body_text = '**Response**\n\nNone'
    else:
        response_desc = 'If successful, this method returns a response body with the following structure:\n\n'
        js_block_header = '.. code-block:: javascript\n\n'
        response_body_message_class_name = method_response.get('$ref')
        js_block_body = get_next_parameter_javascript_row(response_body_message_class_name,
                                                          JS_SPACE + '{\n',
                                                          resource_name=resource,
                                                          method_name=method)
        csv_header = get_csv_table_heading()
        csv_body = get_next_property_table_row(response_body_message_class_name, '', resource_name=resource, method_name=method)
        response_body_text = '**Response**\n\n{}{}{}\n\n{}\n{}'.format(
            response_desc, js_block_header, js_block_body, csv_header, csv_body)
    with open(DEV_DOCUMENTATION_DIRECTORY_PATH + file_name, 'a+') as f:
        f.write(response_body_text)

def write_rst_file_exceptions_section(resource, method):
    '''
    document exceptions thrown for each api method
    '''
    exceptions_json = get_json_file_contents('exceptions_v3')
    file_name = resource + '_' + method + '.rst'
    exceptions_text = '\n\n\n**Exceptions thrown**::\n\n\t'
    exceptions_text += exceptions_json[resource + '_' + method]
    with open(DEV_DOCUMENTATION_DIRECTORY_PATH + file_name, 'a+') as f:
        f.write(exceptions_text)

def main():
    for endpoint, program in zip(('isb_cgc_api', 'isb_cgc_ccle_api', 'isb_cgc_target_api', 'isb_cgc_tcga_api'), ('', '_CCLE', '_TARGET', '_TCGA')):
        set_endpoint_info(endpoint)
        resource_list = [resource for resource in RESP_JSON['resources'].keys()]
        file_name_list = [resource + '_' + method
                          for resource in RESP_JSON['resources'].keys()
                          for method in RESP_JSON['resources'][resource]['methods'].keys()
                          ]
        for file_name in file_name_list:
            create_new_rst_file(file_name)
    
        for resource in resource_list:
            for method in RESP_JSON['resources'][resource]['methods'].keys():
                write_rst_file_header(resource, method, endpoint, program)
                write_rst_file_path_parameters(resource, method)
                write_rst_file_request_body(resource, method, program)
                write_rst_file_response_section(resource, method)
                # write_rst_file_exceptions_section(resource, method)

if __name__ == '__main__':
    main()
