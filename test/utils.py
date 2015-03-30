import unittest
from mock import patch

from google.appengine.ext import ndb, testbed


class BaseTestCase(unittest.TestCase):
    """Base test class which all other test cases should extend."""
    def setUp(self):
        self.addCleanup(patch.stopall)


class DatastoreBaseCase(BaseTestCase):
    """Base test class for dealing with the application and datastore."""
    UNAUTHENTICATED_USER = {
        'user_email': '',
        'user_id': '',
        'is_admin': False
    }

    DEFAULT_USER = {
        'user_email': 'test.user@iastate.edu',
        'user_id': 'test.user-ID',
        'is_admin': False
    }

    ADMIN_USER = {
        'user_email': 'admin.user@iastate.edu',
        'user_id': 'admin.user-ID',
        'is_admin': True
    }

    def setUp(self):
        self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_memcache_stub()
        self.testbed.init_user_stub()
        ndb.get_context().clear_cache()
        self.addCleanup(self.tear_down)

    def tear_down(self):
        self.testbed.deactivate()

    def login(self, user_email, user_id, is_admin):
        """
        Simulate a Google account login.

        :param user_email: simulated user email
        :type  user_email: basestring
        :param user_id: simulated user id
        :type  user_id: basestring
        :param is_admin: whether or not the simulated user is an admin
        :type  is_admin: boolean
        """
        self.testbed.setup_env(
            user_email=user_email,
            user_id=user_id,
            user_is_admin=('1' if is_admin else '0'),
            overwrite=True)
