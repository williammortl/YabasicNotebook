import os
import tempfile
import subprocess
from ipykernel.kernelbase import Kernel

class YabasicKernel(Kernel):
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
