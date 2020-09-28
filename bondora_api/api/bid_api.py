# coding: utf-8

"""
    Bondora API V1

    Bondora API version 1  # noqa: E501

    OpenAPI spec version: v1
    Contact: investor@bondora.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from bondora_api.api_client import ApiClient


class BidApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bid_cancel_bid(self, id, **kwargs):  # noqa: E501
        """Cancel the Bid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bid_cancel_bid(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Bid identificator (required)
        :return: ApiResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bid_cancel_bid_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.bid_cancel_bid_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def bid_cancel_bid_with_http_info(self, id, **kwargs):  # noqa: E501
        """Cancel the Bid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bid_cancel_bid_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Bid identificator (required)
        :return: ApiResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bid_cancel_bid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `bid_cancel_bid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bid/{id}/cancel', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bid_get_bid(self, id, **kwargs):  # noqa: E501
        """Get the Bid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bid_get_bid(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Bid identificator (required)
        :return: ApiResultBid
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bid_get_bid_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.bid_get_bid_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def bid_get_bid_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get the Bid  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bid_get_bid_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: Bid identificator (required)
        :return: ApiResultBid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bid_get_bid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `bid_get_bid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bid/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResultBid',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bid_get_bid_summaries(self, **kwargs):  # noqa: E501
        """Gets list of bids the investor has made.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bid_get_bid_summaries(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int request_bid_status_code: Bid status code
        :param datetime request_start_date: Start date
        :param datetime request_end_date: End date
        :param int request_page_size: Max items in result, up to 20000
        :param int request_page_nr: Result page nr
        :return: ApiResultBids
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bid_get_bid_summaries_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.bid_get_bid_summaries_with_http_info(**kwargs)  # noqa: E501
            return data

    def bid_get_bid_summaries_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of bids the investor has made.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bid_get_bid_summaries_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int request_bid_status_code: Bid status code
        :param datetime request_start_date: Start date
        :param datetime request_end_date: End date
        :param int request_page_size: Max items in result, up to 20000
        :param int request_page_nr: Result page nr
        :return: ApiResultBids
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_bid_status_code', 'request_start_date', 'request_end_date', 'request_page_size', 'request_page_nr']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bid_get_bid_summaries" % key
                )
            params[key] = val
        del params['kwargs']

        if 'request_page_size' in params and params['request_page_size'] > 20000:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_size` when calling `bid_get_bid_summaries`, must be a value less than or equal to `20000`")  # noqa: E501
        if 'request_page_size' in params and params['request_page_size'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_size` when calling `bid_get_bid_summaries`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'request_page_nr' in params and params['request_page_nr'] > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_nr` when calling `bid_get_bid_summaries`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if 'request_page_nr' in params and params['request_page_nr'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_nr` when calling `bid_get_bid_summaries`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_bid_status_code' in params:
            query_params.append(('request.bidStatusCode', params['request_bid_status_code']))  # noqa: E501
        if 'request_start_date' in params:
            query_params.append(('request.startDate', params['request_start_date']))  # noqa: E501
        if 'request_end_date' in params:
            query_params.append(('request.endDate', params['request_end_date']))  # noqa: E501
        if 'request_page_size' in params:
            query_params.append(('request.pageSize', params['request_page_size']))  # noqa: E501
        if 'request_page_nr' in params:
            query_params.append(('request.pageNr', params['request_page_nr']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bids', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResultBids',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def bid_make_bids(self, bid_request, **kwargs):  # noqa: E501
        """Makes bid(s) into specified auction(s).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bid_make_bids(bid_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidRequest bid_request:  (required)
        :return: ApiResultMakeBids
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bid_make_bids_with_http_info(bid_request, **kwargs)  # noqa: E501
        else:
            (data) = self.bid_make_bids_with_http_info(bid_request, **kwargs)  # noqa: E501
            return data

    def bid_make_bids_with_http_info(self, bid_request, **kwargs):  # noqa: E501
        """Makes bid(s) into specified auction(s).  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bid_make_bids_with_http_info(bid_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidRequest bid_request:  (required)
        :return: ApiResultMakeBids
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['bid_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bid_make_bids" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'bid_request' is set
        if ('bid_request' not in params or
                params['bid_request'] is None):
            raise ValueError("Missing the required parameter `bid_request` when calling `bid_make_bids`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'bid_request' in params:
            body_params = params['bid_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/bid', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResultMakeBids',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
