from django.test import SimpleTestCase


# Create your tests here.
class testNearHundo(SimpleTestCase):
    def test_near_hundo_89(self):
        response = self.client.get("/warmup-1/near-hundred/89/")
        self.assertContains(response, "False")

    def test_near_hundo_90(self):
        response = self.client.get("/warmup-1/near-hundred/90/")
        self.assertContains(response, "True")

    def test_near_hundo_93(self):
        response = self.client.get("/warmup-1/near-hundred/93/")
        self.assertContains(response, "True")


class testStringSplosion(SimpleTestCase):
    def test_splo_code(self):
        response = self.client.get("/warmup-2/string-splosion/Code/")
        self.assertContains(response, "CCoCodCode")

    def test_splo_abc(self):
        response = self.client.get("/warmup-2/string-splosion/abc/")
        self.assertContains(response, "aababc")

    def test_splo_ab(self):
        response = self.client.get("/warmup-2/string-splosion/ab/")
        self.assertContains(response, "aab")


class testString2(SimpleTestCase):
    def test_cat(self):
        response = self.client.get("/string-2/catdog/")
        self.assertContains(response, "True")

    def test_catCat(self):
        response = self.client.get("/string-2/catcat/")
        self.assertContains(response, "False")

    def test_catyaddayadda(self):
        response = self.client.get("/string-2/1cat1cadodog/")
        self.assertContains(response, "True")


class testLonesomenum(SimpleTestCase):
    def test1_2_3(self):
        response = self.client.get("/Logic-2/1/2/3/")
        self.assertContains(response, "6")

    def test3_2_3(self):
        response = self.client.get("/Logic-2/3/2/3/")
        self.assertContains(response, "2")

    def test3_3_3(self):
        response = self.client.get("/Logic-2/3/3/3/")
        self.assertContains(response, "0")
