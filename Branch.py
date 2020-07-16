import os
import subprocess
import inquirer


class Branch:
    def __init__(self):
        self.choices = ['task', 'feature', 'hotfix', 'release']

    def __getCurrentWorkingDirectory(self):

        return os.getcwd()

    def __validateItsAGitRepository(self):

        directories = os.listdir(self.__getCurrentWorkingDirectory())

        if '.git' in directories:
            return True
        else:
            print('This is not a Git directory!')
            quit()

    def newBranch(self):

        self.__validateItsAGitRepository()

        print('Creating a new branch')
        prefix = {
            inquirer.Confirm(
                'prefix',
                message = 'Do you want to use a GIT-Flow prefix?',
                default = True
            ),
        }

        prefix_confirmation = inquirer.prompt(prefix)
        if prefix_confirmation['prefix']:
            branch_name = self.__getBranchPrefix()
        else:
            branch_name = self.__getNewBranchName()

        self.__createBranch(branch_name)
        self.__doCheckout(branch_name)

    def __getNewBranchName(self):

        print('Creating new branch!')
        branch = input('Set the branch name: ')

        if branch:
            print('The branch name has been set to: ', branch)
        else:
            quit()

        return branch

    def __getBranchPrefix(self):

        prefixes = [
            inquirer.List(
                'prefix',
                message = 'Which GIT-Flow prefix do you need?',
                choices = self.choices,
            ),
        ]
        answers = inquirer.prompt(prefixes)
        prefix = answers['prefix']

        print('The branch prefix has been set to: ', prefix)

        return '%s/%s' % (prefix, self.__getNewBranchName())

    def __createBranch(self, new_branch):

        subprocess.run(['git', 'branch', new_branch])
        print('The branch %s is created!' % new_branch)

    def __doCheckout(self, new_branch):

        checkout = {
            inquirer.Confirm('checkout',
                             message = 'Do you want to checkout the new branch? ',
                             default = True),
        }
        confirmation = inquirer.prompt(checkout)

        if confirmation['checkout']:
            print('Checking out the new branch!')
            subprocess.run(['git', 'checkout', new_branch])
        else:
            quit()
