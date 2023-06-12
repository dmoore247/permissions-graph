# permissions-graph

## Purpose
Generate a knowledge graph (KG) representation of your Databricks account and workspace metadata. Using this KG representation, perform valuable analyses, including migration planning and execution.


## Setup

The python requirements are specified in the requirements.txt.
Overall, this package uses `databricks-connect==13.*`, `databricks-sdk` and `databricks-sql-connector`


## Testing

The unit tests rely on connecting to a live databricks workspace and account.
Place your credentials into your ~/.databrickscfg
Before running pytest from command line or IDE, ensure this variable is set

export DATABRICKS_CONFIG_PROFILE=<profile name>

