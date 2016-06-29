import requests
import pprint
import json
import sys
import os

JSON_FILE_DIRECTORY = 'endpoints_json_files'


try:
    resp = requests.get('https://api-dot-isb-cgc.appspot.com/_ah/api/discovery/v1/apis/isb_cgc_api/v2/rest')
    RESP_JSON = resp.json()
except:
    with open(JSON_FILE_DIRECTORY + '/resp_json_v2.json', 'r') as f:
        contents = f.read()
    RESP_JSON = json.loads(contents)

DEV_DOCUMENTATION_DIRECTORY_PATH = 'docs/source/sections/progapi/progapi2_develop/'
BASE_URL = RESP_JSON['baseUrl']
JS_SPACE = '  '

# biospecimen_data in sample_details only has the following fields from MetadataItem
SAMPLE_DETAILS_BIOSPECIMEN_DATA_FIELDS = [
    'avg_percent_lymphocyte_infiltration',
    'avg_percent_monocyte_infiltration',
    'avg_percent_necrosis',
    'avg_percent_neutrophil_infiltration',
    'avg_percent_normal_cells',
    'avg_percent_stromal_cells',
    'avg_percent_tumor_cells',
    'avg_percent_tumor_nuclei',
    'batch_number',
    'bcr',
    'days_to_collection',
    'max_percent_lymphocyte_infiltration',
    'max_percent_monocyte_infiltration',
    'max_percent_necrosis',
    'max_percent_neutrophil_infiltration',
    'max_percent_normal_cells',
    'max_percent_stromal_cells',
    'max_percent_tumor_cells',
    'max_percent_tumor_nuclei',
    'min_percent_lymphocyte_infiltration',
    'min_percent_monocyte_infiltration',
    'min_percent_necrosis',
    'min_percent_neutrophil_infiltration',
    'min_percent_normal_cells',
    'min_percent_stromal_cells',
    'min_percent_tumor_cells',
    'min_percent_tumor_nuclei',
    'ParticipantBarcode',
    'Project',
    'SampleBarcode',
    'Study'
]

# clinical_data in patient_details only has the following fields for MetadataItem
PATIENT_DETAILS_CLINICAL_DATA_FIELDS = [
    'age_at_initial_pathologic_diagnosis',
    'anatomic_neoplasm_subdivision',
    'batch_number',
    'bcr',
    'clinical_M',
    'clinical_N',
    'clinical_stage',
    'clinical_T',
    'colorectal_cancer',
    'country',
    'days_to_birth',
    'days_to_death',
    'days_to_initial_pathologic_diagnosis',
    'days_to_last_followup',
    'days_to_submitted_specimen_dx',
    'Study',
    'ethnicity',
    'frozen_specimen_anatomic_site',
    'gender',
    'height',
    'histological_type',
    'history_of_colon_polyps',
    'history_of_neoadjuvant_treatment',
    'history_of_prior_malignancy',
    'hpv_calls',
    'hpv_status',
    'icd_10',
    'icd_o_3_histology',
    'icd_o_3_site',
    'lymphatic_invasion',
    'lymphnodes_examined',
    'lymphovascular_invasion_present',
    'menopause_status',
    'mononucleotide_and_dinucleotide_marker_panel_analysis_status',
    'mononucleotide_marker_panel_analysis_status',
    'neoplasm_histologic_grade',
    'new_tumor_event_after_initial_treatment',
    'number_of_lymphnodes_examined',
    'number_of_lymphnodes_positive_by_he',
    'ParticipantBarcode',
    'pathologic_M',
    'pathologic_N',
    'pathologic_stage',
    'pathologic_T',
    'person_neoplasm_cancer_status',
    'pregnancies',
    'primary_neoplasm_melanoma_dx',
    'primary_therapy_outcome_success',
    'prior_dx',
    'Project',
    'psa_value',
    'race',
    'residual_tumor',
    'tobacco_smoking_history',
    'tumor_tissue_site',
    'tumor_type',
    'weiss_venous_invasion',
    'vital_status',
    'weight',
    'year_of_initial_pathologic_diagnosis'
]


def get_index_of_nth_uppercase_char(a_string, n):
    '''
    Used to find the index of the nth uppercase letter in a string.
    Intended to find the third uppercase letter in a schema name,
    e.g. get_index_of_uppercase('ApiMetadataMetadataItem', 3) returns 11
    or None if there is no third uppercase letter
    '''
    count = 0
    i = 0
    # [letter for letter in a_string if letter.isupper()][n]
    for letter in a_string:
        if letter.isupper():
            count += 1
        if count == n:
            return i
        i += 1
    return None


def get_message_class_list():
    message_class_list = []
    for message_class in RESP_JSON['schemas'].keys():
        message_class_list.append(message_class)
    return sorted(message_class_list, key=lambda s: s[get_index_of_nth_uppercase_char(s, 3):].lower())


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

    # only allow certain fields for patient_details and sample_details methods
    if method_name == 'patient_details' and message_class_name == 'ApiMetadataMetadataItem':
        allowed_keys = set(PATIENT_DETAILS_CLINICAL_DATA_FIELDS).intersection(message_class_properties)
        cleaned_message_class_properties = {k:message_class_properties[k] for k in allowed_keys}
        message_class_properties = cleaned_message_class_properties
    elif method_name == 'sample_details' and message_class_name == 'ApiMetadataMetadataItem':
        allowed_keys = set(SAMPLE_DETAILS_BIOSPECIMEN_DATA_FIELDS).intersection(message_class_properties.keys())
        cleaned_message_class_properties = {k:message_class_properties[k] for k in allowed_keys}
        message_class_properties = cleaned_message_class_properties

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

    # only allow certain fields for patient_details and sample_details methods
    if method_name == 'patient_details' and message_class_name == 'ApiMetadataMetadataItem':
        allowed_keys = set(PATIENT_DETAILS_CLINICAL_DATA_FIELDS).intersection(message_class_properties)
        cleaned_message_class_properties = {k:message_class_properties[k] for k in allowed_keys}
        message_class_propertiesdescription_filename = cleaned_message_class_properties
    elif method_name == 'sample_details' and message_class_name == 'ApiMetadataMetadataItem':
        allowed_keys = set(SAMPLE_DETAILS_BIOSPECIMEN_DATA_FIELDS).intersection(message_class_properties.keys())
        cleaned_message_class_properties = {k:message_class_properties[k] for k in allowed_keys}
        message_class_properties = cleaned_message_class_properties

    sorted_message_class_properties = list(sorted(message_class_properties.iteritems(),
                                                  key=lambda s: s[0].lower()))

    description_filename = message_class_name[get_index_of_nth_uppercase_char(message_class_name, 5):] + '.json'


    with open(JSON_FILE_DIRECTORY + '/' + description_filename, 'r+') as f:
        description_contents = f.read()
        description_json = json.loads(description_contents)


    for key, val in sorted_message_class_properties:
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
            started_string += '\t{level}{key}[], list, "{desc}"\n'\
                .format(level=level, key=key, desc=description_json[key])
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
        example_contents = f.read()

    return json.loads(example_contents)


def write_rst_file_header(resource, method):
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

    example_contents_json = get_json_file_contents('examples_v2')
    api_explorer_example_contents_json = get_json_file_contents('api_explorer_examples_v2')

    example_text = ''
    if example_contents_json.get(file_name):
        example_text = '\n\n**Example**::\n\n\t' + example_contents_json[file_name]

    api_explorer_example_text = ''
    if example_contents_json.get(file_name):
        api_explorer_example_text = "\n\n**API explorer example**:\n\nClick `here <{}/>`_ " \
                                    "to see this endpoint in Google's API explorer.".format(
            api_explorer_example_contents_json[file_name])

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


def write_rst_file_request_body(resource, method):
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
        with open(JSON_FILE_DIRECTORY + '/allowed_values_v2.json', 'r') as f:
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



def main():

    resource_list = [resource for resource in RESP_JSON['resources'].keys()]
    file_name_list = [resource + '_' + method
                      for method in RESP_JSON['resources'][resource]['methods'].keys()
                      for resource in RESP_JSON['resources'].keys()]

    for file_name in file_name_list:
        create_new_rst_file(file_name)

    for resource in resource_list:
        for method in RESP_JSON['resources'][resource]['methods'].keys():
            write_rst_file_header(resource, method)
            write_rst_file_path_parameters(resource, method)
            write_rst_file_request_body(resource, method)
            write_rst_file_response_section(resource, method)


if __name__ == '__main__':
    main()
