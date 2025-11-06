# 2Cents-Capital-Assignment
2Cents Capital Assignment
# Quantitative Trading Portfolio (Quant Finance Assignment)

This repository contains the project setup for a multi-alpha, multi-broker quantitative trading system.

## Project Objective

The goal of this project was to design, build, and test a rigorous, event-driven trading system capable of managing a portfolio of five distinct alphas, with a primary focus on the **scientific replication** of backtest results in a live-sandbox environment.

## Architecture (Track B: Alpha Integrator)

The system was designed using the **"Track B: Alpha Integrator"** approach, leveraging the `nautilus-trader` framework to manage data and execution across Binance, Interactive Brokers, and Zerodha. The full architecture is detailed in the final PDF report.

## Repository Contents

* **/src/**: Contains the Python source code.
    * `test_connection.py`: Initial script for testing broker connectivity (Phase I).
* **/config/**: Contains configuration files.
    * `api_keys.ini`: (Stub) for managing broker API keys (added to `.gitignore`).
* **requirements.txt**: The full list of Python dependencies required for the project.
* **The Final Report (PDF)**: The complete analysis, including the critical **Replication Analysis**, is detailed in the submitted PDF.

## Note on Codebase Status

Due to a persistent local Python environment failure (package resolution and `ModuleNotFoundError` errors) that could not be resolved within the allotted time, the codebase development was halted at Phase I.

As per the assignment's grading criteria, which heavily weights the analysis, the project focus was pivoted to delivering a complete **System Architecture Design** and a **Deep Root-Cause Analysis** of the replication challenge, both of which are contained in the final PDF report.