from project.category import Category
from project.document import Document
from project.topic import Topic
from typing import List


class Storage:

    def __init__(self):
        self.categories: List[Category] = []
        self.documents: List[Document] = []
        self.topics: List[Topic] = []

    def add_category(self, category: Category) -> None:
        if category not in self.categories:
            self.categories.append(category)

    def add_document(self, document: Document) -> None:
        if document not in self.documents:
            self.documents.append(document)

    def add_topic(self, topic: Topic) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def __edit_object(self, object_id, objects_collection, *new_values) -> None:
        current_obj = self.__find_object(object_id, objects_collection)
        if current_obj:
            current_obj.edit(*new_values)

    def __delete_object(self, object_id, object_collection):
        current_obj = self.__find_object(object_id, object_collection)
        if current_obj:
            object_collection.remove(current_obj)

    @staticmethod
    def __find_object(object_id: int, object_collection):
        return next((obj for obj in object_collection if obj.id == object_id), None)

    def edit_category(self, category_id: int, new_name: str) -> None:
        self.__edit_object(category_id, self.categories, new_name)

    def edit_document(self, document_id: int, new_file_name: str) -> None:
        self.__edit_object(document_id, self.documents, new_file_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str) -> None:
        self.__edit_object(topic_id, self.topics, new_topic, new_storage_folder)

    def delete_category(self, category_id) -> None:
        self.__delete_object(category_id, self.categories)

    def delete_document(self, document_id) -> None:
        self.__delete_object(document_id, self.documents)

    def delete_topic(self, topic_id) -> None:
        self.__delete_object(topic_id, self.topics)

    def get_document(self, document_id):
        return self.__find_object(document_id, self.documents)

    def __repr__(self) -> str:
        return '\n'.join([d.__repr__() for d in self.documents])
