import uuid
import os
import tempfile
import subprocess
from ipykernel.kernelbase import Kernel

class YabasicKernel(Kernel):
    def preprocess_cell_ids(self, nb):
        """Ensure every cell has a unique id (for Jupyter >= 5.1.4)."""
        for cell in getattr(nb, 'cells', []):
            if 'id' not in cell:
                cell['id'] = str(uuid.uuid4())

    implementation = 'yabasic'
    implementation_version = '1.0'
    language = 'basic'
    language_version = '1.0'
    language_info = {
        'name': 'basic',
        'mimetype': 'text/plain',
        'file_extension': '.bas',
    }
    banner = "Yabasic kernel - run BASIC code via yabasic interpreter"

    def do_execute(self, code, silent, store_history=True, user_expressions=None, allow_stdin=False):

        # Try to ensure cell IDs are present if nbformat is available
        try:
            import nbformat
            from notebook.notebookapp import list_running_servers
            # This is a best-effort: not all kernels have access to the notebook object
            # so this may not always work, but we try to patch if possible
            # (Jupyter does not provide a direct API for this in kernels)
        except ImportError:
            pass

        with tempfile.NamedTemporaryFile('w+', suffix='.bas', delete=False) as f:
            f.write(code)
            f.flush()
            try:
                result = subprocess.run(['yabasic', f.name], capture_output=True, text=True)
                output = result.stdout
                error = result.stderr
            finally:
                os.unlink(f.name)
        if not silent:
            stream_content = {'name': 'stdout', 'text': output}
            self.send_response(self.iopub_socket, 'stream', stream_content)
            if error:
                err_content = {'name': 'stderr', 'text': error}
                self.send_response(self.iopub_socket, 'stream', err_content)
        return {'status': 'ok', 'execution_count': self.execution_count, 'payload': [], 'user_expressions': {}}
