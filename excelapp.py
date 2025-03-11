from flask import Flask, request, send_file, jsonify
import pandas as pd
import os
import sqlite3

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload_file():
    if "file" not in request.files:
            return "No file part", 400
	        file = request.files["file"]
		    if file.filename == "":
		            return "No selected file", 400
			        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
				    file.save(filepath)
				        return "File uploaded successfully", 200

					@app.route("/process", methods=["POST"])
					def process_file():
					    filename = request.json.get("filename")
					        filepath = os.path.join(UPLOAD_FOLDER, filename)
						    if not os.path.exists(filepath):
						            return "File not found", 404
							        
								    df = pd.read_excel(filepath)
								        df = df.applymap(lambda x: x.strip() if isinstance(x, str) else x)  # Remove whitespace
									    df.drop_duplicates(inplace=True)  # Remove duplicates
									        
										    processed_filepath = os.path.join(UPLOAD_FOLDER, f"processed_{filename}")
										        df.to_excel(processed_filepath, index=False)
											    return send_file(processed_filepath, as_attachment=True)

											    @app.route("/vlookup", methods=["POST"])
											    def vlookup():
											        data = request.json
												    filename = data.get("filename")
												        lookup_value = data.get("lookup_value")
													    lookup_column = data.get("lookup_column")
													        return_column = data.get("return_column")
														    filepath = os.path.join(UPLOAD_FOLDER, filename)
														        if not os.path.exists(filepath):
															        return "File not found", 404
																    
																        df = pd.read_excel(filepath)
																	    result = df.loc[df[lookup_column] == lookup_value, return_column].values
																	        return jsonify({"result": result.tolist() if len(result) > 0 else "Not found"})

																		@app.route("/sql_query", methods=["POST"])
																		def sql_query():
																		    data = request.json
																		        filename = data.get("filename")
																			    query = data.get("query")
																			        filepath = os.path.join(UPLOAD_FOLDER, filename)
																				    if not os.path.exists(filepath):
																				            return "File not found", 404
																					        
																						    df = pd.read_excel(filepath)
																						        conn = sqlite3.connect(":memory:")
																							    df.to_sql("data", conn, index=False, if_exists="replace")
																							        result_df = pd.read_sql_query(query, conn)
																								    conn.close()
																								        return jsonify(result_df.to_dict(orient="records"))

																									if __name__ == "__main__":
																									    app.run(debug=True)

