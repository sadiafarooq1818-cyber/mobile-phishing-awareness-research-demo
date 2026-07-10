# Power BI Dashboard Requirements Document

## Target Audience

- Operations manager
- Commercial analyst
- Sales manager
- Business intelligence team

## Dashboard Purpose

Provide a clear overview of sales and profit performance across regions, product categories and customer segments.

## Functional Requirements

1. Display total sales, total profit, total orders and profit margin.
2. Allow filtering by month, region, product category and customer segment.
3. Show sales and profit trends across time.
4. Compare region-level performance.
5. Identify top products by revenue.
6. Highlight discount and margin risks.
7. Include KPI definitions and assumptions.

## Non-Functional Requirements

- Dashboard should be easy for non-technical users to understand.
- KPI definitions should be consistent across all visuals.
- Dataset should be refreshed using the same schema.
- Visuals should avoid unnecessary clutter.
- Measures should use DAX calculations rather than manual spreadsheet values.

## Data Quality Checks

- Check missing order IDs.
- Validate that sales and profit are numeric.
- Check negative or zero sales values.
- Confirm date formatting is consistent.
- Review unusually high discount values.
- Check duplicate order IDs.

## Data Governance Notes

- Each KPI must have a written definition.
- Refresh frequency should be documented.
- Dataset owner should be identified.
- Assumptions and limitations should be visible to users.

## Dashboard Success Criteria

- Managers can identify sales performance quickly.
- Users can filter results by key business dimensions.
- Trends and outliers are visible without needing raw data.
- Reporting logic is documented and repeatable.

## Relevant Job Skills Demonstrated

- BI dashboard requirements gathering
- Power BI dashboard planning
- Data visualisation principles
- KPI documentation
- Data governance awareness
- Stakeholder communication
- Decision-support reporting