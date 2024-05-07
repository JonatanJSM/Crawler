import requests


class Downloader:

    def download(self, request):
        try:
            response = requests.get(request.url)
            if response.status_code == 200:
                return response
            else:
                print(f"Error al descargar {request.url}. Código de estado: {response.status_code}")
                return None
        except Exception as e:
            print(f"Error al descargar {request.url}: {e}")
            return None
