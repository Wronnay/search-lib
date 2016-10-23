<?php
/* 
 * 	Wronnay Search Library
 *  
 * 	Copyright 2016 Christoph Daniel Miksche
 * 	All rights reserved.
 * 
 * 	License: GNU General Public License
*/

// Set Namespace
namespace WronnaySearchLib;

require_once 'settings.php';

/**
* The Crawler Class
* 
* @author	Christoph Daniel Miksche (Wronnay)
* @date		23.10.2016
* @package 	WronnaySearchLib
* @since	Version 0.1
* 
*/
class Crawler {

	/**
	* Generate a ID of the crawled entry
	* 
	* @author	Christoph Daniel Miksche (Wronnay)
	* @date		23.10.2016
	* @package 	WronnaySearchLib
	* @since	Version 0.1
	* @status 	UNTESTED!
	* 
	* @param	String	$url	The URL of the crawled entry.
	* 
	* @return 	String			An sha1-Hash of the URL & SALT
	*/
	function generateID($url){
		
		return hash('sha1', $url . SALT);
		
	}
	
	/**
	* Get the Links of a Website
	* 
	* @author	Christoph Daniel Miksche (Wronnay)
	* @date		23.10.2016
	* @package 	WronnaySearchLib
	* @since	Version 0.1
	* @status 	WORKS (23.10.2016)
	* 
	* @param	String	$url	The URL which should be crawled.
	* 
	* @return 	Array			A array with the crawled links of the site.
	*/
	function getLinks($url){
		
		// Options for the stream
		$options = array("http" => array("header" => "User-Agent: ".USERAGENT."\r\n"));
		
		// Create the stream
		$context = stream_context_create($options);

		// Get the source code of the website
		$html = file_get_contents($url, false, $context);
		
		// Start array for the links
		$links = array();
		
		// Get the links of the website
		if (preg_match_all('/<a\s+.*?href=[\"\']?([^\"\' >]*)[\"\']?[^>]*>(.*?)<\/a>/si', $html, $links)) {
			$links = $links[1];
		}
 
		return $links;
		
	}
	
}
