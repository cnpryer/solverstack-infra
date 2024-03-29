# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from app import util
from app.api.models.base_model_ import Model
from app.api.models.latitude import Latitude  # noqa: F401,E501
from app.api.models.longitude import Longitude  # noqa: F401,E501
from app.api.models.quantity import Quantity  # noqa: F401,E501


class Demand(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self,
        latitude: Latitude = None,
        longitude: Longitude = None,
        quantity: Quantity = None,
    ):  # noqa: E501
        """Demand - a model defined in Swagger

        :param latitude: The latitude of this Demand.  # noqa: E501
        :type latitude: Latitude
        :param longitude: The longitude of this Demand.  # noqa: E501
        :type longitude: Longitude
        :param quantity: The quantity of this Demand.  # noqa: E501
        :type quantity: Quantity
        """
        self.swagger_types = {
            "latitude": Latitude,
            "longitude": Longitude,
            "quantity": Quantity,
        }

        self.attribute_map = {
            "latitude": "latitude",
            "longitude": "longitude",
            "quantity": "quantity",
        }
        self._latitude = latitude
        self._longitude = longitude
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt) -> "Demand":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Demand of this Demand.  # noqa: E501
        :rtype: Demand
        """
        return util.deserialize_model(dikt, cls)

    @property
    def latitude(self) -> Latitude:
        """Gets the latitude of this Demand.


        :return: The latitude of this Demand.
        :rtype: Latitude
        """
        return self._latitude

    @latitude.setter
    def latitude(self, latitude: Latitude):
        """Sets the latitude of this Demand.


        :param latitude: The latitude of this Demand.
        :type latitude: Latitude
        """

        self._latitude = latitude

    @property
    def longitude(self) -> Longitude:
        """Gets the longitude of this Demand.


        :return: The longitude of this Demand.
        :rtype: Longitude
        """
        return self._longitude

    @longitude.setter
    def longitude(self, longitude: Longitude):
        """Sets the longitude of this Demand.


        :param longitude: The longitude of this Demand.
        :type longitude: Longitude
        """

        self._longitude = longitude

    @property
    def quantity(self) -> Quantity:
        """Gets the quantity of this Demand.


        :return: The quantity of this Demand.
        :rtype: Quantity
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: Quantity):
        """Sets the quantity of this Demand.


        :param quantity: The quantity of this Demand.
        :type quantity: Quantity
        """
        if quantity is None:
            raise ValueError(
                "Invalid value for `quantity`, must not be `None`"
            )  # noqa: E501

        self._quantity = quantity
