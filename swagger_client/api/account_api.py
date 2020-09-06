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

from swagger_client.api_client import ApiClient


class AccountApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def account_get_active(self, **kwargs):  # noqa: E501
        """Gets list of your investments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get_active(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime request_loan_issued_date_from: Loan issued start date from
        :param datetime request_loan_issued_date_to: Loan issued start date to
        :param float request_principal_min: Remaining principal amount min
        :param float request_principal_max: Remaining principal amount max
        :param float request_interest_min: Interest rate min
        :param float request_interest_max: Interest rate max
        :param int request_length_max: Loan lenght min
        :param int request_length_min: Loan lenght max
        :param float request_late_principal_amount_min: Principal debt amount min
        :param float request_late_principal_amount_max: Principal debt amount max
        :param datetime request_debt_occured_on_from: Principal debt started date from
        :param datetime request_debt_occured_on_to: Principal debt started date to
        :param datetime request_debt_occured_on_for_secondary_from: Interest debt started date from
        :param datetime request_debt_occured_on_for_secondary_to: Interest debt started date to
        :param datetime request_defaulted_date_from: Defaulted date from
        :param datetime request_defaulted_date_to: Defaulted date to
        :param datetime request_rescheduled_from: Defaulted date from
        :param datetime request_rescheduled_to: Defaulted date to
        :param datetime request_sold_date_from: When it was sold on Secondary market from
        :param datetime request_sold_date_to: When it was sold on Secondary market to
        :param datetime request_purchase_date_from: When you received the investment Auctions/Secondary market from
        :param datetime request_purchase_date_to: When you received the investment Auctions/Secondary market to
        :param datetime request_next_payment_date_to: Next payment date to
        :param datetime request_next_payment_date_from: Next payment date from
        :param datetime request_last_payment_date_from: Last payment date from
        :param datetime request_last_payment_date_to: Last payment date to
        :param list[str] request_countries: Two letter iso code for country of origin: EE, ES, FI
        :param list[str] request_ratings: Bondora's rating: AA, A, B, C, D, E, F, HR
        :param int request_credit_score_min: Minimum credit score
        :param int request_credit_score_max: Maximum credit score
        :param str request_user_name: Borrower's username
        :param list[int] request_loan_status_code: Loan status code              <para>0 Reserved</para><para>2 Current</para><para>3 Cancelled</para><para>100 Overdue</para><para>5 60+ days overdue</para><para>4 Repaid</para><para>8 Released</para>
        :param int request_income_verification_status: Income verification type
        :param int request_loan_debt_management_stage: Latest debt management stage
        :param int request_loan_debt_management_stage_type: Latest debt management stage type
        :param datetime request_loan_debt_management_date_active_from: Latest debt management date active from
        :param datetime request_loan_debt_management_date_active_to: Latest debt management date active to
        :param int request_auction_bid_type: Auction bid type
        :param int request_sales_status: Second market sale status              <para>NULL All active</para><para>0 Bought investments</para><para>1 Sold investments</para><para>2 Investment is on sale</para><para>3 Investment is not on sale</para>
        :param bool request_is_in_repayment: Search only active in repayment loans, StatusCodes (2, 5, 100)
        :param int request_page_size: Max items in result, up to 50000
        :param int request_page_nr: Result page nr
        :return: ApiResultMyInvestments
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_get_active_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.account_get_active_with_http_info(**kwargs)  # noqa: E501
            return data

    def account_get_active_with_http_info(self, **kwargs):  # noqa: E501
        """Gets list of your investments  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get_active_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime request_loan_issued_date_from: Loan issued start date from
        :param datetime request_loan_issued_date_to: Loan issued start date to
        :param float request_principal_min: Remaining principal amount min
        :param float request_principal_max: Remaining principal amount max
        :param float request_interest_min: Interest rate min
        :param float request_interest_max: Interest rate max
        :param int request_length_max: Loan lenght min
        :param int request_length_min: Loan lenght max
        :param float request_late_principal_amount_min: Principal debt amount min
        :param float request_late_principal_amount_max: Principal debt amount max
        :param datetime request_debt_occured_on_from: Principal debt started date from
        :param datetime request_debt_occured_on_to: Principal debt started date to
        :param datetime request_debt_occured_on_for_secondary_from: Interest debt started date from
        :param datetime request_debt_occured_on_for_secondary_to: Interest debt started date to
        :param datetime request_defaulted_date_from: Defaulted date from
        :param datetime request_defaulted_date_to: Defaulted date to
        :param datetime request_rescheduled_from: Defaulted date from
        :param datetime request_rescheduled_to: Defaulted date to
        :param datetime request_sold_date_from: When it was sold on Secondary market from
        :param datetime request_sold_date_to: When it was sold on Secondary market to
        :param datetime request_purchase_date_from: When you received the investment Auctions/Secondary market from
        :param datetime request_purchase_date_to: When you received the investment Auctions/Secondary market to
        :param datetime request_next_payment_date_to: Next payment date to
        :param datetime request_next_payment_date_from: Next payment date from
        :param datetime request_last_payment_date_from: Last payment date from
        :param datetime request_last_payment_date_to: Last payment date to
        :param list[str] request_countries: Two letter iso code for country of origin: EE, ES, FI
        :param list[str] request_ratings: Bondora's rating: AA, A, B, C, D, E, F, HR
        :param int request_credit_score_min: Minimum credit score
        :param int request_credit_score_max: Maximum credit score
        :param str request_user_name: Borrower's username
        :param list[int] request_loan_status_code: Loan status code              <para>0 Reserved</para><para>2 Current</para><para>3 Cancelled</para><para>100 Overdue</para><para>5 60+ days overdue</para><para>4 Repaid</para><para>8 Released</para>
        :param int request_income_verification_status: Income verification type
        :param int request_loan_debt_management_stage: Latest debt management stage
        :param int request_loan_debt_management_stage_type: Latest debt management stage type
        :param datetime request_loan_debt_management_date_active_from: Latest debt management date active from
        :param datetime request_loan_debt_management_date_active_to: Latest debt management date active to
        :param int request_auction_bid_type: Auction bid type
        :param int request_sales_status: Second market sale status              <para>NULL All active</para><para>0 Bought investments</para><para>1 Sold investments</para><para>2 Investment is on sale</para><para>3 Investment is not on sale</para>
        :param bool request_is_in_repayment: Search only active in repayment loans, StatusCodes (2, 5, 100)
        :param int request_page_size: Max items in result, up to 50000
        :param int request_page_nr: Result page nr
        :return: ApiResultMyInvestments
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_loan_issued_date_from', 'request_loan_issued_date_to', 'request_principal_min', 'request_principal_max', 'request_interest_min', 'request_interest_max', 'request_length_max', 'request_length_min', 'request_late_principal_amount_min', 'request_late_principal_amount_max', 'request_debt_occured_on_from', 'request_debt_occured_on_to', 'request_debt_occured_on_for_secondary_from', 'request_debt_occured_on_for_secondary_to', 'request_defaulted_date_from', 'request_defaulted_date_to', 'request_rescheduled_from', 'request_rescheduled_to', 'request_sold_date_from', 'request_sold_date_to', 'request_purchase_date_from', 'request_purchase_date_to', 'request_next_payment_date_to', 'request_next_payment_date_from', 'request_last_payment_date_from', 'request_last_payment_date_to', 'request_countries', 'request_ratings', 'request_credit_score_min', 'request_credit_score_max', 'request_user_name', 'request_loan_status_code', 'request_income_verification_status', 'request_loan_debt_management_stage', 'request_loan_debt_management_stage_type', 'request_loan_debt_management_date_active_from', 'request_loan_debt_management_date_active_to', 'request_auction_bid_type', 'request_sales_status', 'request_is_in_repayment', 'request_page_size', 'request_page_nr']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_get_active" % key
                )
            params[key] = val
        del params['kwargs']

        if 'request_page_size' in params and params['request_page_size'] > 50000:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_size` when calling `account_get_active`, must be a value less than or equal to `50000`")  # noqa: E501
        if 'request_page_size' in params and params['request_page_size'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_size` when calling `account_get_active`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'request_page_nr' in params and params['request_page_nr'] > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_nr` when calling `account_get_active`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if 'request_page_nr' in params and params['request_page_nr'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_nr` when calling `account_get_active`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_loan_issued_date_from' in params:
            query_params.append(('request.loanIssuedDateFrom', params['request_loan_issued_date_from']))  # noqa: E501
        if 'request_loan_issued_date_to' in params:
            query_params.append(('request.loanIssuedDateTo', params['request_loan_issued_date_to']))  # noqa: E501
        if 'request_principal_min' in params:
            query_params.append(('request.principalMin', params['request_principal_min']))  # noqa: E501
        if 'request_principal_max' in params:
            query_params.append(('request.principalMax', params['request_principal_max']))  # noqa: E501
        if 'request_interest_min' in params:
            query_params.append(('request.interestMin', params['request_interest_min']))  # noqa: E501
        if 'request_interest_max' in params:
            query_params.append(('request.interestMax', params['request_interest_max']))  # noqa: E501
        if 'request_length_max' in params:
            query_params.append(('request.lengthMax', params['request_length_max']))  # noqa: E501
        if 'request_length_min' in params:
            query_params.append(('request.lengthMin', params['request_length_min']))  # noqa: E501
        if 'request_late_principal_amount_min' in params:
            query_params.append(('request.latePrincipalAmountMin', params['request_late_principal_amount_min']))  # noqa: E501
        if 'request_late_principal_amount_max' in params:
            query_params.append(('request.latePrincipalAmountMax', params['request_late_principal_amount_max']))  # noqa: E501
        if 'request_debt_occured_on_from' in params:
            query_params.append(('request.debtOccuredOnFrom', params['request_debt_occured_on_from']))  # noqa: E501
        if 'request_debt_occured_on_to' in params:
            query_params.append(('request.debtOccuredOnTo', params['request_debt_occured_on_to']))  # noqa: E501
        if 'request_debt_occured_on_for_secondary_from' in params:
            query_params.append(('request.debtOccuredOnForSecondaryFrom', params['request_debt_occured_on_for_secondary_from']))  # noqa: E501
        if 'request_debt_occured_on_for_secondary_to' in params:
            query_params.append(('request.debtOccuredOnForSecondaryTo', params['request_debt_occured_on_for_secondary_to']))  # noqa: E501
        if 'request_defaulted_date_from' in params:
            query_params.append(('request.defaultedDateFrom', params['request_defaulted_date_from']))  # noqa: E501
        if 'request_defaulted_date_to' in params:
            query_params.append(('request.defaultedDateTo', params['request_defaulted_date_to']))  # noqa: E501
        if 'request_rescheduled_from' in params:
            query_params.append(('request.rescheduledFrom', params['request_rescheduled_from']))  # noqa: E501
        if 'request_rescheduled_to' in params:
            query_params.append(('request.rescheduledTo', params['request_rescheduled_to']))  # noqa: E501
        if 'request_sold_date_from' in params:
            query_params.append(('request.soldDateFrom', params['request_sold_date_from']))  # noqa: E501
        if 'request_sold_date_to' in params:
            query_params.append(('request.soldDateTo', params['request_sold_date_to']))  # noqa: E501
        if 'request_purchase_date_from' in params:
            query_params.append(('request.purchaseDateFrom', params['request_purchase_date_from']))  # noqa: E501
        if 'request_purchase_date_to' in params:
            query_params.append(('request.purchaseDateTo', params['request_purchase_date_to']))  # noqa: E501
        if 'request_next_payment_date_to' in params:
            query_params.append(('request.nextPaymentDateTo', params['request_next_payment_date_to']))  # noqa: E501
        if 'request_next_payment_date_from' in params:
            query_params.append(('request.nextPaymentDateFrom', params['request_next_payment_date_from']))  # noqa: E501
        if 'request_last_payment_date_from' in params:
            query_params.append(('request.lastPaymentDateFrom', params['request_last_payment_date_from']))  # noqa: E501
        if 'request_last_payment_date_to' in params:
            query_params.append(('request.lastPaymentDateTo', params['request_last_payment_date_to']))  # noqa: E501
        if 'request_countries' in params:
            query_params.append(('request.countries', params['request_countries']))  # noqa: E501
            collection_formats['request.countries'] = 'multi'  # noqa: E501
        if 'request_ratings' in params:
            query_params.append(('request.ratings', params['request_ratings']))  # noqa: E501
            collection_formats['request.ratings'] = 'multi'  # noqa: E501
        if 'request_credit_score_min' in params:
            query_params.append(('request.creditScoreMin', params['request_credit_score_min']))  # noqa: E501
        if 'request_credit_score_max' in params:
            query_params.append(('request.creditScoreMax', params['request_credit_score_max']))  # noqa: E501
        if 'request_user_name' in params:
            query_params.append(('request.userName', params['request_user_name']))  # noqa: E501
        if 'request_loan_status_code' in params:
            query_params.append(('request.loanStatusCode', params['request_loan_status_code']))  # noqa: E501
            collection_formats['request.loanStatusCode'] = 'multi'  # noqa: E501
        if 'request_income_verification_status' in params:
            query_params.append(('request.incomeVerificationStatus', params['request_income_verification_status']))  # noqa: E501
        if 'request_loan_debt_management_stage' in params:
            query_params.append(('request.loanDebtManagementStage', params['request_loan_debt_management_stage']))  # noqa: E501
        if 'request_loan_debt_management_stage_type' in params:
            query_params.append(('request.loanDebtManagementStageType', params['request_loan_debt_management_stage_type']))  # noqa: E501
        if 'request_loan_debt_management_date_active_from' in params:
            query_params.append(('request.loanDebtManagementDateActiveFrom', params['request_loan_debt_management_date_active_from']))  # noqa: E501
        if 'request_loan_debt_management_date_active_to' in params:
            query_params.append(('request.loanDebtManagementDateActiveTo', params['request_loan_debt_management_date_active_to']))  # noqa: E501
        if 'request_auction_bid_type' in params:
            query_params.append(('request.auctionBidType', params['request_auction_bid_type']))  # noqa: E501
        if 'request_sales_status' in params:
            query_params.append(('request.salesStatus', params['request_sales_status']))  # noqa: E501
        if 'request_is_in_repayment' in params:
            query_params.append(('request.isInRepayment', params['request_is_in_repayment']))  # noqa: E501
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
            '/api/v1/account/investments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResultMyInvestments',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_get_balance(self, **kwargs):  # noqa: E501
        """Gets your account balance information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get_balance(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApiResultMyAccountBalance
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_get_balance_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.account_get_balance_with_http_info(**kwargs)  # noqa: E501
            return data

    def account_get_balance_with_http_info(self, **kwargs):  # noqa: E501
        """Gets your account balance information  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get_balance_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: ApiResultMyAccountBalance
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_get_balance" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKey']  # noqa: E501

        return self.api_client.call_api(
            '/api/v1/account/balance', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResultMyAccountBalance',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def account_get_event_log(self, **kwargs):  # noqa: E501
        """Gets events that have been made with this application (related to current access token)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get_event_log(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime request_event_date_from: Start datetime
        :param datetime request_event_date_to: end datetime
        :param int request_event_type: Event type
        :param str request_ip_address: IP address
        :param int request_page_size: Max items in result, up to 20000
        :param int request_page_nr: Result page nr
        :return: ApiResultEventLog
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.account_get_event_log_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.account_get_event_log_with_http_info(**kwargs)  # noqa: E501
            return data

    def account_get_event_log_with_http_info(self, **kwargs):  # noqa: E501
        """Gets events that have been made with this application (related to current access token)  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.account_get_event_log_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param datetime request_event_date_from: Start datetime
        :param datetime request_event_date_to: end datetime
        :param int request_event_type: Event type
        :param str request_ip_address: IP address
        :param int request_page_size: Max items in result, up to 20000
        :param int request_page_nr: Result page nr
        :return: ApiResultEventLog
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request_event_date_from', 'request_event_date_to', 'request_event_type', 'request_ip_address', 'request_page_size', 'request_page_nr']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method account_get_event_log" % key
                )
            params[key] = val
        del params['kwargs']

        if 'request_page_size' in params and params['request_page_size'] > 20000:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_size` when calling `account_get_event_log`, must be a value less than or equal to `20000`")  # noqa: E501
        if 'request_page_size' in params and params['request_page_size'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_size` when calling `account_get_event_log`, must be a value greater than or equal to `1`")  # noqa: E501
        if 'request_page_nr' in params and params['request_page_nr'] > 2147483647:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_nr` when calling `account_get_event_log`, must be a value less than or equal to `2147483647`")  # noqa: E501
        if 'request_page_nr' in params and params['request_page_nr'] < 1:  # noqa: E501
            raise ValueError("Invalid value for parameter `request_page_nr` when calling `account_get_event_log`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}

        query_params = []
        if 'request_event_date_from' in params:
            query_params.append(('request.eventDateFrom', params['request_event_date_from']))  # noqa: E501
        if 'request_event_date_to' in params:
            query_params.append(('request.eventDateTo', params['request_event_date_to']))  # noqa: E501
        if 'request_event_type' in params:
            query_params.append(('request.eventType', params['request_event_type']))  # noqa: E501
        if 'request_ip_address' in params:
            query_params.append(('request.ipAddress', params['request_ip_address']))  # noqa: E501
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
            '/api/v1/eventlog', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ApiResultEventLog',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
