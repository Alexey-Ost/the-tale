
import smart_imports

smart_imports.all()


class RequestProcessor(utils_views.BaseViewProcessor):
    ARG_REQUEST_CLASS = utils_views.ProcessorArgument()

    def preprocess(self, context):
        try:
            context.tt_request = self.request_class.FromString(context.django_request.body)
        except:
            raise utils_views.ViewError(code='common.wrong_tt_post_data',
                                       message='Переданы неверные данные',
                                       http_status=utils_relations.HTTP_STATUS.INTERNAL_SERVER_ERROR)


class SecretProcessor(utils_views.BaseViewProcessor):
    ARG_SECRET = utils_views.ProcessorArgument()

    def preprocess(self, context):
        if context.tt_request.secret != self.secret:
            raise utils_views.ViewError(code='common.wrong_tt_secret',
                                       message='У Вас нет прав для проведения данной операции',
                                       http_status=utils_relations.HTTP_STATUS.INTERNAL_SERVER_ERROR)


class ProtobufOk(utils_views.BaseResponse):

    def __init__(self, http_mimetype='application/protobuf', **kwargs):
        super().__init__(http_mimetype=http_mimetype, **kwargs)

    def complete(self, context):
        self.content = self.content.SerializeToString()
        return super().complete(context)
