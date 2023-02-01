import speech_commands as sp
from ubinascii import a2b_base64, b2a_base64

data = a2b_base64('AgkKAQvQ/PrKFP/y47Ud6s7w5xTYJvT9E+Xc+fTM/K688fTh2QH3+wYf694R8f80INgY89DVKt/Q5yr72vjX9Ngq/eiz39rE5ge/97n2zfa9Csa55wPn6r3QKga7r9axzNvd/dQC4wO4ENbZGuISGhoB0+vWyfbx9e8F38DNAwsm3Cw9/t/YzvT/veft3e3yxMzc3tvo2OoN7Am70/Yg8PMZ5csBDOr84xzZ2Be89QINFRjSAMD4BvLaBwHVGOg54Rco7+7zFt/Q97rj7wQy+gzf8eXf9uDlvQUE6tm9IfDu6Sf53vDiA8kg7NEGAhK/Au7oDyTZN80a+iAW7sn7+f34FuviC/bm9QbGEC/HKvq7uhfdzuU41d7uHBTU2xYLG9cNA/wG4RfTKRDMAubmCkUj6ePy+fDd+usDE9H37PDg3+oPLh7G2dw49dY1GP0gs83ny/5K9+MZ9eXW/8n+A9P/GBPyAtIN+P3avTMbIscJRdjUGd4TCNAjCQUhBwzu9PEgHREWFe7nINn+PsfoH9j4Ngn96x8W+hT2tRIC7CAOFR4D8RMPA/Ij8PUHAvzW5/8BKf8BDiLgJN0P/hPcMOjaLvj+Qvrj4A/oDS3e5vYV9Rvw7iX09xcBAbgH0CQK4foDBQYZ0vXdHNQg+xP78BYcADsc89367tQc9N/i9Qoh4x0JOTjv8vcfA90y3Pf56Nf2z+HrJBLFCDUb+O7SKtj79S/56/L70xTixvXQBQ8rDMU26B4OIRsPIerWALgQE/fm+eIRN/Uf6Djw/g27FRIRIBAX4zIu+/jdNz4eCi8bQP4jGv8ZIw7mUxjiExHkEAQqFfL94yMNN+IKOCwrIMDQESYT4RUMFOIxDT9K+ywqCDwYMRYYKCA/7yMtNTP2Gu382yH75+wQ90AEEgbB8fEN5z0GL/koMggVvB5GDMQw/RcR9u8RHzQgAfzzE/tDGtQsCisCICY6JOoxEf7iHjnsJCQF6BDN9uNR+Qo63PLlGMYw6xTyQhb4CP8cLufsDu7nC0X5RTAY5EH57xvZzwhP+yn06zcbDwv9DxI1++Et3N0q5fko5xjzJ0rU/b89CghI3dEj8Pg7CdbD3hrx1iAiDeAuz1BQ//XrL/kcst71QekMDBsk9zMB40kCCs0TKhMF/iPoUNM93ykb997yQPP3/vgSCMnjPQgEABwwLeNHBv77I8z8D0P1Q/Ic/OjwIwvEDlL42wYaO+Uj9w4BGyY/BPXn+DzXMfrvGhDk7knb9vgA+x70Bf4J4hjtCxjhHREU/RkBAhI8EkMX6Cf/EvgD0u3yEyoMLSXvPfsv7gko+gDfH+oD+gLjNBbr1PX9v8H8Dw8V8SUD0NIGLSEv6wneHOry8xsQAdcdIQEk7PIMLSYh+AT35jROsR3mLNwBKNbz1BwSDAEC//0mOw3iAsHYLPHvDxQpM+wFJ+4REtwmQ+74FCIZUATqKjbd8vQLJQzW/ybW6BgvOtT0Dh7R+fQu7iAXyfS89BIs/f8N+w759RzhET0JC+8c6u4c/gjY/v3yAfi+Qg==')
sp.init(data)
labels = ["lili","[OTHER]"]
feature = bytearray(732)

def predict(audio):
    result = sp.predict(audio, 0, 0)
    return (labels[result // 1000], result % 1000)