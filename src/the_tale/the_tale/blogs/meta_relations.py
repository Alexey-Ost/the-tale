
import smart_imports

smart_imports.all()


class Post(meta_relations_objects.MetaType):
    __slots__ = ('caption', '_object__lazy')
    TYPE = 1
    TYPE_CAPTION = 'Произведение'

    def __init__(self, caption, **kwargs):
        super(Post, self).__init__(**kwargs)
        self.caption = caption
        self._object__lazy = None

    @property
    def url(self):
        return utils_urls.url('blogs:posts:show', self.id)

    @classmethod
    def create_from_object(cls, post):
        object = cls(id=post.id, caption=post.caption)
        object._object__lazy = post
        return object

    @classmethod
    def create_removed(cls):
        return cls(id=None, caption='неизвестное произведение')

    @utils_decorators.lazy_property
    def object(self):
        from . import prototypes
        return prototypes.PostPrototype.get_by_id(self.id)

    @classmethod
    def create_from_id(cls, id):
        from . import prototypes

        post = prototypes.PostPrototype.get_by_id(id)

        if post is None:
            return cls.create_removed()

        return cls.create_from_object(post)

    @classmethod
    def create_from_ids(cls, ids):
        from . import prototypes

        return [cls(id=id, caption=caption) for id, caption in prototypes.PostPrototype._db_filer(ids__in=ids).values_list('id', 'caption')]


class IsAbout(meta_relations_objects.MetaRelation):
    TYPE = 1
