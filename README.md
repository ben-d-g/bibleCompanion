# bibleCompanion

## Introduction

This project will be a framework for a Bible Companion app. The idea is to provide a structure in which thoughts can be noted and organised.

Once this framework is in place I would like to package it nicely, but for now, baby steps.

## Technology

I will first create a model of bibleCompanion in Python, then in Java. This is really just for a bit of practice in both languages.

## Structure

bibleCompanion will consist of a Notebook filled with Notes, which can be organised, filtered, and searched using various tags and categories.

### Notes

A Note will consist of some content, and some tags (Bible reference, theme, custom criteria, anything else that may be of use), and an identifier.

Tags should be able to be accessed easily, but should also be flexible (not all Notes require all tags to be filled). Perhaps a dictionary is best to implement this?

### Notebook

The Notebook will be a collection of instances of Note, along with the capabilities to search through them and apply filters.