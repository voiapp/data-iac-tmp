"""A Google Cloud Python Pulumi program"""

import pulumi
from pulumi_gcp import storage
from pulumi import automation

# # Create a GCP resource (Storage Bucket)
# bucket = storage.Bucket('my-bucket', location="US")
#
# # Export the DNS name of the bucket
# pulumi.export('bucket_name', bucket.url)
#
#

# wrapper-call
# it will get the parent directory name
# it should create a new stack (if it doesn't exist)
from pathlib import Path

from importlib.resources import path
from pathlib import Path

list_of_parents = [tmp_addr.parts[1] for tmp_addr in list(Path('..').glob('**/Pulumi.yaml'))]

set_of_parents = set(list_of_parents)

project_name = "service-a"
# We use a simple stack name here, but recommend using auto.fully_qualified_stack_name for maximum specificity.
stack_name = ""


# stack_name = auto.fully_qualified_stack_name("myOrgOrUser", project_name, stack_name)

# create or select a stack matching the specified name and project.
# this will set up a workspace with everything necessary to run our inline program (pulumi_program)®
def pulumi_program():
    print('inside')
    # print(storage.get_bucket('my-bucket-59e43bb').name)
    index_content = """
         <html>
             <head><title>Hello S3</title><meta charset="UTF-8"></head>
             <body>
                 <p>Hello, world!</p>
                 <p>Made with ❤️ with <a href="https://pulumi.com">Pulumi</a></p>
             </body>
         </html>
         """

    bucket = storage.Bucket('my-bucket', location='us', project='voi-data-warehouse-stage')
    bucket = storage.get_bucket('my-bucket-59e43bb')
    bucketObject = storage.BucketObject(
        'index2.html',
        bucket=bucket,
        source=pulumi.StringAsset(index_content)
    )


stack = automation.create_or_select_stack(stack_name=stack_name,
                                          project_name=project_name,
                                          program=pulumi_program)
stack.preview()
stack.preview(on_output=print)
# pulumi up
print("updating stack...")
up_res = stack.up(on_output=print)
print(f"update summary: \n{json.dumps(up_res.summary.resource_changes, indent=4)}")
# print(f"website url: {up_res.outputs['website_url'].value}")

print('history')
print(stack.history())
