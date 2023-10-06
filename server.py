from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__, static_url_path='/static')
print(__name__)


@app.route('/')
def my_home():
    return render_template("./index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as database:
#         email = data["email"]
#         subject = data["subject"]
#         message = data["message"]
#         file = database.write(f"\n{email}, {subject}, {message}")


def write_to_csv(data):
    csv_file_path = "database.csv"

    with open(csv_file_path, mode="a", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row
        header_row = ["email", "subject", "message"]
        csv_writer.writerow(header_row)

        # Write data rows
        data_row = [data["email"], data["subject"], data["message"]]
        csv_writer.writerow(data_row)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thankyou.html')
        except Exception as e:
            return f"An error occurred: {str(e)}"
    else:
        return 'something went wrong, Try Again!'


if __name__ == '__main__':
    app.run()