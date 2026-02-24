from __future__ import annotations


def normalize_navigation_url(url: str) -> str:
	"""Normalize user-provided CLI URL input for navigation commands."""
	if url.startswith(('http://', 'https://', 'file://')):
		return url
	if url.startswith(('http:', 'https:')):
		scheme, rest = url.split(':', 1)
		return f'{scheme}://{rest.lstrip("/")}'
	return 'https://' + url
