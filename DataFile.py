# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 01:58:34 2021

@author: rames
"""
from pydantic import BaseModel

class Data(BaseModel):
    account_amount_added_12_24m: int
    account_days_in_dc_12_24m: float
    account_days_in_rem_12_24m: float
    account_days_in_term_12_24m: float
    account_incoming_debt_vs_paid_0_24m: float
    account_status: float
    age: int
    avg_payment_span_0_12m: float
    merchant_category: str
    merchant_group: str
    has_paid: int
    max_paid_inv_0_24m: float
    num_active_div_by_paid_inv_0_12m: float
    num_active_inv: int
    num_arch_dc_0_12m: int
    num_arch_dc_12_24m: int
    num_arch_ok_0_12m: int
    num_arch_ok_12_24m: int
    num_arch_rem_0_12m: int
    num_arch_written_off_0_12m: float
    num_arch_written_off_12_24m: float
    num_unpaid_bills: int
    status_last_archived_0_24m: int
    status_2nd_last_archived_0_24m: int
    status_max_archived_0_24_months: int
    recovery_debt: int
    sum_capital_paid_account_0_12m: int
    sum_paid_inv_0_12m: int
    time_hours: float