<<<<<<< HEAD

from core.command_factory import CommandFactory


=======
from core.command_factory import CommandFactory

>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
class Engine:
    def __init__(self, factory: CommandFactory):
        self._command_factory = factory

    def start(self):
<<<<<<< HEAD
        output = []
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'end':
                    break

                output.append(self._process_command(input_line))
            except ValueError as err:
                output.append(err.args[0])

        print('\n####################\n'.join(output))

    def _process_command(self, input_line):
        cmd_name, *params = input_line.split()

=======
        while True:
            try:
                input_line = input()
                if input_line.lower() == 'exit':
                    break

                result = self._process_command(input_line)
                print(result)  
            except ValueError as err:
                print(err.args[0])  

    def _process_command(self, input_line):
        cmd_name, *params = input_line.split()
>>>>>>> 9a4c026 (Created truck editted app_data, route,package)
        return self._command_factory.create(cmd_name).execute(params)