# coding: utf-8

"""
    Swagger Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: apiteam@swagger.io
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Pet(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'category': 'Category',
        'name': 'str',
        'photo_urls': 'list[str]',
        'tags': 'list[Tag]',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'category': 'category',
        'name': 'name',
        'photo_urls': 'photoUrls',
        'tags': 'tags',
        'status': 'status'
    }

    def __init__(self, id=None, category=None, name=None, photo_urls=None, tags=None, status=None):  # noqa: E501
        """Pet - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._category = None
        self._name = None
        self._photo_urls = None
        self._tags = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if category is not None:
            self.category = category
        self.name = name
        self.photo_urls = photo_urls
        if tags is not None:
            self.tags = tags
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this Pet.  # noqa: E501


        :return: The id of this Pet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Pet.


        :param id: The id of this Pet.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def category(self):
        """Gets the category of this Pet.  # noqa: E501


        :return: The category of this Pet.  # noqa: E501
        :rtype: Category
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Pet.


        :param category: The category of this Pet.  # noqa: E501
        :type: Category
        """

        self._category = category

    @property
    def name(self):
        """Gets the name of this Pet.  # noqa: E501


        :return: The name of this Pet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Pet.


        :param name: The name of this Pet.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def photo_urls(self):
        """Gets the photo_urls of this Pet.  # noqa: E501


        :return: The photo_urls of this Pet.  # noqa: E501
        :rtype: list[str]
        """
        return self._photo_urls

    @photo_urls.setter
    def photo_urls(self, photo_urls):
        """Sets the photo_urls of this Pet.


        :param photo_urls: The photo_urls of this Pet.  # noqa: E501
        :type: list[str]
        """
        if photo_urls is None:
            raise ValueError("Invalid value for `photo_urls`, must not be `None`")  # noqa: E501

        self._photo_urls = photo_urls

    @property
    def tags(self):
        """Gets the tags of this Pet.  # noqa: E501


        :return: The tags of this Pet.  # noqa: E501
        :rtype: list[Tag]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this Pet.


        :param tags: The tags of this Pet.  # noqa: E501
        :type: list[Tag]
        """

        self._tags = tags

    @property
    def status(self):
        """Gets the status of this Pet.  # noqa: E501

        pet status in the store  # noqa: E501

        :return: The status of this Pet.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Pet.

        pet status in the store  # noqa: E501

        :param status: The status of this Pet.  # noqa: E501
        :type: str
        """
        allowed_values = ["available", "pending", "sold"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Pet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Pet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
