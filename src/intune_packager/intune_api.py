import os
import msal
import requests

AUTHORITY = 'https://login.microsoftonline.com/common'
SCOPES = ['https://graph.microsoft.com/.default']
GRAPH_URL = 'https://graph.microsoft.com/beta'
CLIENT_ID = os.environ.get('INTUNE_CLIENT_ID', 'YOUR_CLIENT_ID')


class IntuneClient:
    def __init__(self):
        self.app = msal.PublicClientApplication(client_id=CLIENT_ID, authority=AUTHORITY)
        self.token = None

    def authenticate(self):
        if not self.token:
            flow = self.app.initiate_device_flow(scopes=SCOPES)
            if 'message' in flow:
                print(flow['message'])
            self.token = self.app.acquire_token_by_device_flow(flow)
        return self.token

    def upload_win32_app(self, file_path: str, install_cmd: str, uninstall_cmd: str):
        token = self.authenticate()
        access_token = token.get('access_token')
        headers = {
            'Authorization': f'Bearer {access_token}',
            'Content-Type': 'application/json'
        }
        data = {
            'displayName': os.path.basename(file_path),
            'description': 'Uploaded via Intune Packager',
            'installCommandLine': install_cmd,
            'uninstallCommandLine': uninstall_cmd
        }
        print('Uploading metadata to Intune...')
        response = requests.post(f'{GRAPH_URL}/deviceAppManagement/mobileApps', headers=headers, json=data)
        response.raise_for_status()
        print('Upload finished.')
