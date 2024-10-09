# MIT License
#
# Copyright (c) 2024 DeRuneLabs
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import tyra.utils.constant as constant
import tyra.utils.license as license_desc
from string import Template

license_name: object = Template(license_desc)
data_license: list = [data for data in constant.LICENSE_LIST]


def generate(license_name: str, author_name: str, year: int) -> None:
    """
    Generate license and write to file called name LICENSE

    Parameter:
        license_name(str): license name
        author_name(str): author name
        year(int): license year
    """
    if isinstance(license_name, str) or isinstance(author_name, str) or isinstance(year, int):
        if license_name.upper() in constant.LICENSE_LIST:
            license_name_info: str = f"{constant.GREEN}Generate {constant.RESET} {license_name.capitalize()} License..."
            if license_name.upper() == "MIT":
                print(license_name_info)
                with open("LICENSE", "w") as generate_license:
                    license_name_template = Template(license_desc.open_license_file(license_name))
                    generate_license_template = license_name_template.safe_substitute(year=str(year), author=author_name)
                    generate_license.write(generate_license_template)
                print("Success!")
            if license_name.upper() == "GNU":
                print(license_name_info)
                with open("LICENSE", "w") as generate_license:
                    generate_license.write(license_desc.open_license_file(license_name))
            if license_name.upper() == "APACHE":
                print(f"Generate {license_name} license...")
                with open("LICENSE", "w") as generate_license:
                    license_name_template = Template(license_desc.open_license_file(license_name))
                    generate_license_template = license_name_template.safe_substitute(year=str(year), author=author_name)
                    generate_license.write(generate_license_template)
            if license_name.upper() == "UNLINCENSE":
                print(license_name_info)
                with open("LICENSE", "w") as generate_license:
                    license_gen = license_desc.open_license_file(license_name)
                    generate_license.write(license_gen)
            if license_name.upper() == "ISC":
                print(license_name_info)
                with open("LICENSE", "w") as generate_license:
                    license_name_template = Template(license_desc.open_license_file(license_name))
                    generate_license_template = license_name_template.safe_substitute(year=str(year), author=author_name)
                    generate_license.write(generate_license_template)
        else:
            print(f"{constant.RED} License not found {constant.RESET}")
    else:
        raise TypeError("license name, author name must str and year must be int")
