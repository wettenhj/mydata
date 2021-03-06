class DuplicateKey(Exception):
    def __init__(self, message):
        super(DuplicateKey, self).__init__(message)


class MultipleObjectsReturned(Exception):
    def __init__(self, message, url=None, response=None):
        super(MultipleObjectsReturned, self).__init__(message)

        self.url = url
        self.response = response

    def GetUrl(self):
        return self.url

    def GetResponse(self):
        return self.response


class DoesNotExist(Exception):
    def __init__(self, message, url=None, response=None, modelClass=None):
        super(DoesNotExist, self).__init__(message)

        self.url = url
        self.response = response
        self.modelClass = modelClass

    def GetUrl(self):
        return self.url

    def GetResponse(self):
        return self.response

    def GetModelClass(self):
        return self.modelClass


class Unauthorized(Exception):
    def __init__(self, message, url=None, response=None):
        super(Unauthorized, self).__init__(message)

        self.url = url
        self.response = response

    def GetUrl(self):
        return self.url

    def GetResponse(self):
        return self.response


class InternalServerError(Exception):
    def __init__(self, message, url=None, response=None):
        super(InternalServerError, self).__init__(message)

        self.url = url
        self.response = response

    def GetUrl(self):
        return self.url

    def GetResponse(self):
        return self.response


class SshException(Exception):
    def __init__(self, message, returncode=None):
        super(SshException, self).__init__(message)
        self.returncode = returncode


class StagingHostRefusedSshConnection(SshException):
    def __init__(self, message):
        super(StagingHostRefusedSshConnection, self).__init__(message)


class StagingHostSshPermissionDenied(SshException):
    def __init__(self, message):
        super(StagingHostSshPermissionDenied, self).__init__(message)


class ScpException(SshException):
    def __init__(self, message, command=None, returncode=None):
        super(ScpException, self).__init__(message)
        self.command = command
        self.returncode = returncode


class NoActiveNetworkInterface(Exception):
    def __init__(self, message):
        super(NoActiveNetworkInterface, self).__init__(message)


class BrokenPipe(Exception):
    def __init__(self, message):
        super(BrokenPipe, self).__init__(message)


class IncompatibleMyTardisVersion(Exception):
    def __init__(self, message):
        super(IncompatibleMyTardisVersion, self).__init__(message)


class PrivateKeyDoesNotExist(Exception):
    def __init__(self, message):
        super(PrivateKeyDoesNotExist, self).__init__(message)


class InvalidFolderStructure(Exception):
    def __init__(self, message):
        super(InvalidFolderStructure, self).__init__(message)


class MissingMyDataAppOnMyTardisServer(Exception):
    def __init__(self, message):
        super(MissingMyDataAppOnMyTardisServer, self).__init__(message)


class StorageBoxAttributeNotFound(Exception):
    def __init__(self, storageBox, key):
        message = "Key '%s' not found in attributes for storage box '%s'" \
            % (key, storageBox.GetName())
        super(StorageBoxAttributeNotFound, self).__init__(message)


class StorageBoxOptionNotFound(Exception):
    def __init__(self, storageBox, key):
        message = "Key '%s' not found in options for storage box '%s'" \
            % (key, storageBox.GetName())
        super(StorageBoxOptionNotFound, self).__init__(message)
