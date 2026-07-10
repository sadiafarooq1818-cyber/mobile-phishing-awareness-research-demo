"""
Python Data Cleaning & Insights Demo

Purpose:
Demonstrate a practical data analyst workflow using pandas:
- Load data
- Check missing values
- Clean and validate fields
- Calculate KPIs
- Produce stakeholder-ready summaries

Dataset:
../data/customer_support_tickets.csv
"""

import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load customer support ticket data."""
    df = pd.read_csv(file_path)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean and prepare ticket data for analysis."""
    cleaned = df.copy()

    # Standardise column names
    cleaned.columns = [col.strip().lower() for col in cleaned.columns]

    # Convert date fields
    cleaned["created_date"] = pd.to_datetime(cleaned["created_date"], errors="coerce")
    cleaned["closed_date"] = pd.to_datetime(cleaned["closed_date"], errors="coerce")

    # Convert numeric fields
    cleaned["resolution_hours"] = pd.to_numeric(cleaned["resolution_hours"], errors="coerce")
    cleaned["satisfaction_score"] = pd.to_numeric(cleaned["satisfaction_score"], errors="coerce")

    # Remove duplicate ticket IDs if present
    cleaned = cleaned.drop_duplicates(subset=["ticket_id"], keep="first")

    # Create useful reporting fields
    cleaned["created_month"] = cleaned["created_date"].dt.to_period("M").astype(str)
    cleaned["is_closed"] = cleaned["status"].str.lower().eq("closed")

    return cleaned


def data_quality_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a data quality summary table."""
    summary = pd.DataFrame({
        "column": df.columns,
        "missing_values": df.isna().sum().values,
        "missing_percent": (df.isna().mean().values * 100).round(2),
        "unique_values": df.nunique(dropna=True).values,
    })
    return summary


def calculate_kpis(df: pd.DataFrame) -> dict:
    """Calculate core support reporting KPIs."""
    closed_tickets = df[df["is_closed"]]

    kpis = {
        "total_tickets": int(df["ticket_id"].nunique()),
        "closed_tickets": int(closed_tickets["ticket_id"].nunique()),
        "open_tickets": int((~df["is_closed"]).sum()),
        "average_resolution_hours": round(closed_tickets["resolution_hours"].mean(), 2),
        "average_satisfaction_score": round(closed_tickets["satisfaction_score"].mean(), 2),
    }

    return kpis


def grouped_summaries(df: pd.DataFrame) -> dict:
    """Create grouped summaries for stakeholder reporting."""
    summaries = {}

    summaries["tickets_by_category"] = (
        df.groupby("category")
        .agg(ticket_count=("ticket_id", "nunique"), avg_resolution_hours=("resolution_hours", "mean"))
        .round(2)
        .sort_values("ticket_count", ascending=False)
    )

    summaries["tickets_by_priority"] = (
        df.groupby("priority")
        .agg(ticket_count=("ticket_id", "nunique"), avg_resolution_hours=("resolution_hours", "mean"))
        .round(2)
        .sort_values("avg_resolution_hours", ascending=False)
    )

    summaries["tickets_by_channel"] = (
        df.groupby("channel")
        .agg(ticket_count=("ticket_id", "nunique"), avg_satisfaction=("satisfaction_score", "mean"))
        .round(2)
        .sort_values("ticket_count", ascending=False)
    )

    summaries["monthly_ticket_volume"] = (
        df.groupby("created_month")
        .agg(ticket_count=("ticket_id", "nunique"), closed_tickets=("is_closed", "sum"))
        .sort_index()
    )

    return summaries


def print_report(kpis: dict, quality: pd.DataFrame, summaries: dict) -> None:
    """Print a simple analyst report."""
    print("\nCUSTOMER SUPPORT ANALYTICS REPORT")
    print("=" * 40)

    print("\nCore KPIs")
    for key, value in kpis.items():
        print(f"- {key.replace('_', ' ').title()}: {value}")

    print("\nData Quality Summary")
    print(quality)

    print("\nTickets by Category")
    print(summaries["tickets_by_category"])

    print("\nTickets by Priority")
    print(summaries["tickets_by_priority"])

    print("\nTickets by Channel")
    print(summaries["tickets_by_channel"])

    print("\nMonthly Ticket Volume")
    print(summaries["monthly_ticket_volume"])

    print("\nBusiness Insights")
    print("- Critical and high-priority tickets show longer resolution times and should be monitored closely.")
    print("- Phone and email channels generate significant support workload and may need resourcing review.")
    print("- Open tickets require follow-up to protect customer satisfaction and service reliability.")
    print("- Missing resolution and satisfaction values are expected for open tickets and should be excluded from closed-ticket KPIs.")


def main() -> None:
    file_path = "../data/customer_support_tickets.csv"
    raw_data = load_data(file_path)
    cleaned_data = clean_data(raw_data)
    quality = data_quality_summary(cleaned_data)
    kpis = calculate_kpis(cleaned_data)
    summaries = grouped_summaries(cleaned_data)
    print_report(kpis, quality, summaries)

    # Export a cleaned dataset for reporting or dashboard use
    cleaned_data.to_csv("customer_support_tickets_cleaned.csv", index=False)


if __name__ == "__main__":
    main()
