
import pandas as pd
from flask import Flask, render_template
from pathlib import Path

app = Flask(__name__)

lwd = pd.read_csv(
    Path(__file__).parent / "livwell175.csv"
)

one_country_bool = lwd["country_name"] == "Malawi"
one_country_data = lwd.loc[one_country_bool]

years = one_country_data["year"].tolist()
secondary_education = one_country_data[
    "ED_attainment_secondary_p"
].tolist()
secondary_education_completed = one_country_data[
    "ED_attainment_secondary_completed_p"
].tolist()


@app.route("/")
def home():
    return render_template(
        "index.html",
        years=years,
        secondary_education=secondary_education,
        secondary_education_completed=secondary_education_completed
    )


if __name__ == "__main__":
    app.run(debug=True)
