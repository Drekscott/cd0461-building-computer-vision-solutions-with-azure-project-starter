from azure.ai.formrecognizer import DocumentModelAdministrationClient
from azure.core.credentials import AzureKeyCredential

endpoint = ""
credential = AzureKeyCredential("")

document_model_admin_client = DocumentModelAdministrationClient(endpoint, credential)

container_sas_url = ""  # training documents uploaded to blob storage
poller = document_model_admin_client.begin_build_document_model(
    # For more information about build_mode, see: https://aka.ms/azsdk/formrecognizer/buildmode
    build_mode="template", blob_container_url=container_sas_url, model_id="boarding-pass-model"
)
model = poller.result()

print("Model ID: {}".format(model.model_id))
print("Description: {}".format(model.description))
print("Model created on: {}\n".format(model.created_on))
print("Doc types the model can recognize:")
for name, doc_type in model.doc_types.items():
    print("\nDoc Type: '{}' which has the following fields:".format(name))
    for field_name, confidence in doc_type.field_confidence.items():
        print("Field: '{}' has confidence score {}".format(field_name, confidence))