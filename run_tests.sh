#!/usr/bin/env bash
pytest -s -vvv --cov=workingless --cov-report term-missing tests
