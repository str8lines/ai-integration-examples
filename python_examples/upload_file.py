import os

from auth import URL_BASE_SERVER, authorized_request


def upload_file(file_path: str) -> dict:
    """
    Upload a file to the file collection.

    The file is stored and a file record is created. The returned record's '_id'
    can then be referenced elsewhere (for example, in a scenario's input_file_ids).

    Args:
        file_path: Path to the file on disk to upload.

    Returns:
        dict: The created file record, including its '_id'.
    """
    url = f"{URL_BASE_SERVER}/file/upload_single"

    file_name = os.path.basename(file_path)
    with open(file_path, 'rb') as f:
        files = {'file': (file_name, f)}
        response = authorized_request('POST', url, files=files)

    if not response.ok:
        print(response.status_code, response.content)
        raise ValueError('Unable to upload file.', response.content)

    return response.json()


if __name__ == '__main__':
    # upload an image and print the resulting file id
    uploaded = upload_file('image.png')
    print('Uploaded file id:', uploaded.get('_id'))
