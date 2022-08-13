package main

import (
	"archive/zip"
	"os"
)

func ZipHandler(path string) {
	archive, err := os.Create("handler.zip")
	if err != nil {
		panic(err)
	}
	defer archive.Close()
	zipWriter := zip.NewWriter(archive)

	_, err = zipWriter.Create(path)
	if err != nil {
		panic(err)
	}
}
