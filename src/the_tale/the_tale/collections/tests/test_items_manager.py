
import smart_imports

smart_imports.all()


class ItemsManagerTests(utils_testcase.TestCase):

    def setUp(self):
        super(ItemsManagerTests, self).setUp()

        game_logic.create_test_map()

        self.account_1 = self.accounts_factory.create_account()

        self.account_1_items = prototypes.AccountItemsPrototype.get_by_account_id(self.account_1.id)

        self.collection_1 = prototypes.CollectionPrototype.create(caption='collection_1', description='description_1')
        self.collection_2 = prototypes.CollectionPrototype.create(caption='collection_2', description='description_2', approved=True)

        self.kit_1 = prototypes.KitPrototype.create(collection=self.collection_1, caption='kit_1', description='description_1')
        self.kit_2 = prototypes.KitPrototype.create(collection=self.collection_2, caption='kit_2', description='description_2', approved=True)
        self.kit_3 = prototypes.KitPrototype.create(collection=self.collection_2, caption='kit_3', description='description_3', approved=True)

        self.item_1_1 = prototypes.ItemPrototype.create(kit=self.kit_1, caption='item_1_1', text='text_1_1', approved=False)
        self.item_1_2 = prototypes.ItemPrototype.create(kit=self.kit_1, caption='item_1_2', text='text_1_2', approved=True)
        self.item_2_1 = prototypes.ItemPrototype.create(kit=self.kit_2, caption='item_2_1', text='text_2_1', approved=True)
        self.item_2_2 = prototypes.ItemPrototype.create(kit=self.kit_2, caption='item_2_2', text='text_2_2', approved=False)
        self.item_3_1 = prototypes.ItemPrototype.create(kit=self.kit_3, caption='item_3_1', text='text_3_1', approved=True)

        self.account_1_items.add_item(self.item_1_2)
        self.account_1_items.save()

        self.worker = amqp_environment.environment.workers.items_manager
        self.worker.initialize()

    def test_add_items__not_tasks(self):
        self.worker.add_items()
        self.account_1_items.reload()
        self.assertEqual(len(self.account_1_items.items), 1)

    def test_add_items(self):
        prototypes.GiveItemTaskPrototype.create(account_id=self.account_1.id, item_id=self.item_2_1.id)

        self.assertFalse(self.account_1_items.has_item(self.item_2_1))

        self.worker.add_items()

        self.account_1_items.reload()

        self.assertTrue(self.account_1_items.has_item(self.item_2_1))
        self.assertEqual(prototypes.GiveItemTaskPrototype._db_count(), 0)
