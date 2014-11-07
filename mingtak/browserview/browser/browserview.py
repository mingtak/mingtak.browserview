# -*- coding: utf-8 -*-
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api
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
        self.scriptStr_1 = """
            <script type="text/javascript" async="true" defer="true">
                $(document).ready(function(){
                    $('#"""
        self.scriptStr_2 = """').click(function(){
                        $('#"""
        self.scriptStr_3 = """').load('/changeState?id="""
        self.scriptStr_4 = """');
                    });
                });
            </script>"""
        return self.template()


class ChangeState(BrowserView):
    def __call__(self):
        catalog = self.context.portal_catalog
        brain = catalog(id=self.request['id'])[0]
        item = brain.getObject()
        if brain.review_state == 'published':
            api.content.transition(obj=item, transition='reject')
            item.reindexObject(idxs=["review_state"])
            return '<span style="color:red">狀態: Private</span>'
        else:
            api.content.transition(obj=item, transition='publish')
            item.reindexObject(idxs=["review_state"])
            return '<span style="color:green">狀態: Published</span>'


class ChangeSubject(BrowserView):
    """ 輸入new, old, 將所有cj.product.cjproduct的subecct[0]為old的，改為new,並 reindexObject() """
    def __call__(self):
        catalog = self.context.portal_catalog
        request = self.request
        brain = catalog({'portal_type':'cj.product.cjproduct',
                         'Subject':request['old']})
        count = 0
        for item in brain:
            if item.Subject[0] == request['old']:
                newSubjectList = list(item.Subject)
                newSubjectList[0] = request['new']
                obj = item.getObject()
                obj.setSubject(tuple(newSubjectList))
                obj.reindexObject(idxs=['Subject'])
                count += 1
        return '已完成 %s 筆資料變更' % count
