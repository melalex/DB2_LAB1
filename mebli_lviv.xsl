<?xml version="1.0" encoding="UTF-8" ?>

<xsl:stylesheet version="1.0" 
        xmlns:xsl="http://www.w3.org/1999/XSL/Transform" 
        xmlns="http://www.w3.org/1999/xhtml">
    <xsl:output method="xml" indent="yes"
        doctype-public="-//W3C//DTD XHTML 1.0 Strict//EN" 
        doctype-system="http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd"/>
    
    <xsl:template match="/">
        <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
            <head>
                <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
                <title>mebli-lviv.com.ua</title>
                <style type="text/css">
                    h1          { font-size: 26px;  margin: 15px 0px 5px 0px;  border-bottom: 5px solid black; }
                    td, th      { width: 40%; border: 1px solid silver; padding: 10px }
                    td:first-child, th:first-child  { width: 20% } 
                    table       { width: 650px }
                </style>
            </head>
            <body>
                <xsl:apply-templates/>
            </body>
        </html>
    </xsl:template>
    
    <xsl:template match="product_type">
		<xsl:variable name="url" select="@type_url"/>
        <h1>Product type:<a href="{$url}"><xsl:value-of select="$url"/></a></h1>
		<xsl:apply-templates/>
    </xsl:template>
	
	<xsl:template match="product">
		<xsl:variable name="url" select="@product_url"/>
        <h3>Product:<a href="{$url}"><xsl:value-of select="$url"/></a></h3>
		<p><xsl:value-of select="main_description/text()"/></p>
		<table>
            <tr><th>Description</th><th>Image</th><th>Price</th></tr>
            <xsl:apply-templates select="equipment"/>
        </table>
	</xsl:template>
        
	<xsl:template match="equipment">
		<xsl:variable name="scr" select="image/@scr"/>
		<tr>
			<td><p><xsl:value-of select=".//description/text()"/></p></td>
			<td><img scr="{$scr}" alt="{$scr}" width="125" vspace="5" align="absmiddle" hspace="5"/></td>
			<td><p><xsl:value-of select=".//price/text()"/></p></td>
		</tr>
	</xsl:template>
	
</xsl:stylesheet>