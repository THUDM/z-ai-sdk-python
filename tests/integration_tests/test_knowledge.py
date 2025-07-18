from __future__ import annotations

import logging
import logging.config
import os

import pytest

import zai
from zai import ZaiClient


@pytest.fixture(scope='class')
def test_server():
	class SharedData:
		client = ZaiClient()
		test_knowledge_document_id = None
		test_knowledge_id = None

	return SharedData()


class TestZaiClientKnowledgeServer:
	def test_logs(self, logging_conf):
		logging.config.dictConfig(logging_conf)  # type: ignore

	def test_knowledge_create(self, test_server):
		try:
			result = test_server.client.knowledge.create(
				embedding_id=1,
				name='test',
				description='test',
				background='blue',
				icon='question',
			)
			print(result)
			test_server.test_knowledge_id = result.id

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_document_create(self, test_server, test_file_path):
		try:
			result = test_server.client.knowledge.document.create(
				file=open(os.path.join(test_file_path, 'file.xlsx'), 'rb'),
				purpose='retrieval',
				knowledge_id=test_server.test_knowledge_id,
				sentence_size=202,
			)
			print(result)
			test_server.test_knowledge_document_id = result.successInfos[0].documentId

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_modify(self, test_server):
		try:
			result = test_server.client.knowledge.modify(
				knowledge_id=test_server.test_knowledge_id,
				embedding_id=1,
				name='test1',
				background='red',
				icon='book',
			)
			print(result)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_query(self, test_server):
		try:
			result = test_server.client.knowledge.query()
			print(result)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_used(self, test_server):
		try:
			result = test_server.client.knowledge.used()
			print(result)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_document_retrieve(self, test_server, test_file_path):
		try:
			result = test_server.client.knowledge.document.retrieve(test_server.test_knowledge_document_id)
			print(result)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_document_edit(self, test_server):
		try:
			result = test_server.client.knowledge.document.edit(
				document_id=test_server.test_knowledge_document_id,
				knowledge_type='1',
				sentence_size=204,
			)
			print(result)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_document_list(self, test_server):
		try:
			result = test_server.client.knowledge.document.list(test_server.test_knowledge_id, purpose='retrieval')
			print(result)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_document_delete(self, test_server):
		try:
			file1 = test_server.client.knowledge.document.delete(test_server.test_knowledge_document_id)
			print(file1)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)

	def test_knowledge_delete(self, test_server):
		try:
			result = test_server.client.knowledge.delete(knowledge_id=test_server.test_knowledge_id)
			print(result)

		except zai.core._errors.APIRequestFailedError as err:
			print(err)
		except zai.core._errors.APIInternalError as err:
			print(err)
		except zai.core._errors.APIStatusError as err:
			print(err)
