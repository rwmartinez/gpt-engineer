
from auth0.v3.authentication import GetToken
from auth0.v3.management import Auth0

# Auth0 configuration
auth0_domain = 'your-auth0-domain.auth0.com'
auth0_client_id = 'your-auth0-client-id'
auth0_client_secret = 'your-auth0-client-secret'
auth0_audience = 'your-auth0-audience'
auth0_get_token = GetToken(auth0_domain)
auth0_token = auth0_get_token.client_credentials(auth0_client_id, auth0_client_secret, auth0_audience)
auth0_mgmt_api = Auth0(auth0_domain, auth0_token['access_token'])