#Author: Michael Elgin

#File to create GUI interface for making files

import os
import PySimpleGUI as psg

from Serval import Serval

class GUI():

	def __init__(self):
		self.serval = Serval()

	def refresh_file_list(self, fileListBox):
		accessibleFilesList = []
		for file in os.listdir(self.serval.outputDirectory):
			if self.serval.read(file) != None:
				accessibleFilesList.append(file)
			else:
				continue
		fileListBox.update(accessibleFilesList)

	def run(self):

		#Misc elements
		workingDirectoryText = psg.Text("Set working directory: ")
		workingDirectoryField = psg.Input(
			readonly=True,
			key="workingDirectoryField",
			expand_x=True,
		)
		passwordField = psg.InputText(password_char="*", key="passwordField")
		refreshButton = psg.Button("Refresh Files and Password", key="refreshButton")
		fileListBox = psg.Listbox([], expand_x=True, expand_y=True, key="fileListBox")
		contentBox = psg.Multiline(expand_x=True, expand_y=True, key="contentBox")
		quitButton = psg.Button("Quit")
		feedbackText = psg.Text("Feedback is here! =)")

		#CRUD elements
		createText = psg.Text("Create New File:")
		createField = psg.InputText(key="createField")
		createButton = psg.Button("Create")
		readButton = psg.Button("Read")
		updateButton = psg.Button("Update")
		deleteButton = psg.Button("Delete")

		column = psg.Column([ #Stuff not to be available unless directory set
			[fileListBox, contentBox],
			[quitButton, readButton, updateButton, deleteButton],
			[createText, createField, createButton],
			[feedbackText]
		], visible=False, expand_x=True, expand_y=True)

		layout = [
			[psg.FolderBrowse(), workingDirectoryField],
			[psg.Text("Password:"), passwordField],
			[refreshButton],
			[column],
		]

		window = psg.Window("Secure Encrypted Repository of Valuable Asset Language", layout, resizable=True)

		while True:
			event, values = window.read()

			feedbackText.update("") #Default if no new message.

			if event in (psg.WIN_CLOSED, "Quit"):
				break

			if event == "refreshButton":
				self.serval.set_output_directory(values["workingDirectoryField"])
				self.serval.set_checked_password(values["passwordField"])
				self.refresh_file_list(fileListBox)
				feedbackText.update(
					value="Refreshed - showing files accessible with current password." + (
						("\n--Password WARNINGS--\n" + "\n".join(self.serval.get_warnings()))\
						if len(self.serval.get_warnings()) != 0 else ""
					)
				)
				if values["workingDirectoryField"] != "":
					column.update(visible=True)
			elif event == "Create":
				if values["createField"]  != "":
					if (self.serval.create(values["createField"])):
						self.refresh_file_list(fileListBox)
						createField.update(value="")
						feedbackText.update(value="Created.")
					else:
						feedbackText.update(value="File not created - already exists.")
				else:
					feedbackText.update(value="Create field cannot be empty.")
			elif event == "Read":
				try:
					fileName = values["fileListBox"][0]
					readData = self.serval.read(fileName)
					contentBox.update(value=(readData if readData != None else ""))
					feedbackText.update(value="Showing contents of " + fileName)
				except IndexError:
					feedbackText.update(value="No file selected.")
			elif event == "Update":
				try:
					fileName = values["fileListBox"][0]
					self.serval.update(fileName, values["contentBox"])
					feedbackText.update(value=fileName + " updated.")
				except IndexError:
					feedbackText.update(value="No file selected.")
			elif event == "Delete":
				try:
					fileName = values["fileListBox"][0]
					if (self.serval.delete(fileName)):
						self.refresh_file_list(fileListBox)
						feedbackText.update(value="Deleted " + fileName)
					else:
						feedbackText.update(value=fileName + " not deleted.")
				except IndexError: #Nothing selected from the box
					feedbackText.update(value="No file selected.")

def main():
	GUI().run()

if __name__ == "__main__":
	main()
