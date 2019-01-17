<?xml version="1.0" encoding="UTF-8" ?>

<xsl:stylesheet version="2.0" exclude-result-prefixes="xs xdt err fn"
	xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:xs="http://www.w3.org/2001/XMLSchema"
	xmlns:fn="http://www.w3.org/2005/xpath-functions" xmlns:xdt="http://www.w3.org/2005/xpath-datatypes"
	xmlns:err="http://www.w3.org/2005/xqt-errors">
	<xsl:output method="xml" indent="yes" />
	<xsl:strip-space elements="*" />

	<xsl:template match="Requirements">
		<xsl:copy>
			<xsl:apply-templates>
				<!-- this is to sort -->
			</xsl:apply-templates>
		</xsl:copy>
		<!-- count rules -->
	</xsl:template>

	<xsl:template match="*">
		<xsl:copy>
			<xsl:apply-templates />
		</xsl:copy>
	</xsl:template>

	<!-- template Requirement -->

    <!-- hide rules -->

	<!--  this is to add empty elements Requirements/Requirement when the element Requirements doesn't contain any Requirement child -->
	<!-- useful for the conversion to Json, to keep the JSON structure constant upon empty data in the xml -->
	<xsl:template match="Requirements[not(Requirement)]">
		<Requirements>
			<Requirement></Requirement>
			<xsl:apply-templates />
		</Requirements>
	</xsl:template>
</xsl:stylesheet>