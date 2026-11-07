# Specify the Storage Account
storage_account = "adlsdbricksdevjapanes"

# Configure the Authentication Type
spark.conf.set(
    f"fs.azure.account.auth.type.{storage_account}.dfs.core.windows.net",
    "OAuth"
)

# Specify the OAuth Authentication Provider
spark.conf.set(
    f"fs.azure.account.oauth.provider.type.{storage_account}.dfs.core.windows.net",
    "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider"
)

# Specify the Application (Client) ID
spark.conf.set(
    f"fs.azure.account.oauth2.client.id.{storage_account}.dfs.core.windows.net",
    "f7f2536c-4359-4649-a847-00bcd32812d3"
)

# Specify the Client Secret
spark.conf.set(
    f"fs.azure.account.oauth2.client.secret.{storage_account}.dfs.core.windows.net",
    dbutils.secrets.get(
        scope="adls-dev-scope",
        key="client-secret"
    )
)

# Specify the OAuth Endpoint
spark.conf.set(
    f"fs.azure.account.oauth2.client.endpoint.{storage_account}.dfs.core.windows.net",
    "https://login.microsoftonline.com/bc5e7416-4572-4999-a9e2-8e2436e6cf8e/oauth2/token"
)