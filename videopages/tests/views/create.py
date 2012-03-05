# -*- coding: UTF-8 -*-
from django.core.urlresolvers import reverse
from base import BaseTestCase
from videopages.models import VideoPage

__author__ = 'Razzhivin Alexander'
__email__ = 'admin@httpbots.com'


class VideoPageTestCase(BaseTestCase):

    def test_create(self):
        self.set_edit_video_user_permissions()
        self.assertEquals(0, VideoPage.objects.count())
        url = reverse("videopages_create", args=[self.user.username])
        response = self.client.post(url)
        self.failUnlessEqual(response.status_code, 302)
        self.assertEquals(1, VideoPage.objects.count())