# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
import logging


logger = logging.getLogger("cj.product.productimport")

class GetOnsaleData(BrowserView):
    template = ViewPageTemplateFile("template/getonsaledata.pt")
    def __call__(self):
        return self.template()


class GetVacataionData(BrowserView):
    template = ViewPageTemplateFile("template/getvacationdata.pt")
    def __call__(self):
        return self.template()


class GetDressData(BrowserView):
    template = ViewPageTemplateFile("template/getdressdata.pt")
    def __call__(self):
        return self.template()


class GetBeautyData(BrowserView):
    template = ViewPageTemplateFile("template/getbeautydata.pt")
    def __call__(self):
        return self.template()


class GetHealthData(BrowserView):
    template = ViewPageTemplateFile("template/gethealthdata.pt")
    def __call__(self):
        return self.template()


class GetEntertainmentData(BrowserView):
    template = ViewPageTemplateFile("template/getentertainmentdata.pt")
    def __call__(self):
        return self.template()


class GetProductList(BrowserView):
    template = ViewPageTemplateFile("template/getproductlist.pt")
    def __call__(self):
        return self.template()
