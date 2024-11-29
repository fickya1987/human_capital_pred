
from config import app_config  
import data
import tab_capacity
import tab_summary
import tab_attrition
import tab_promotion  # Newly added promotion module
import utils
import filters

import streamlit as st


def main():
    ### setup app-wide configuration
    utils.setup_app(app_config)

    ### load data
    df_hr = data.load_transform(app_config.data_file)

    ### apply session specific active filters
    df_hr = filters.apply(df_hr)

    ### setup app structure
    exec_summary, capacity_analysis, attrition_analysis, promotion_analysis = utils.create_tabs(
        ["EXECUTIVE SUMMARY 📝", "CAPACITY ANALYSIS 🚀", "ATTRITION ANALYSIS 🏃‍♂️", "PROMOTION ANALYSIS 📈"]
    )
    with exec_summary:
        tab_summary.render(df_hr)
    with capacity_analysis:
        tab_capacity.render(df_hr)
    with attrition_analysis:
        tab_attrition.render(df_hr)
    with promotion_analysis:
        tab_promotion.render(df_hr)


if __name__ == "__main__":
    main()
