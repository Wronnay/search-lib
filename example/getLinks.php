<?php
/* 
 * 	Wronnay Search Library
 *  
 * 	Copyright 2016 Christoph Daniel Miksche
 * 	All rights reserved.
 * 
 * 	License: GNU General Public License
*/

// Load the lib
require_once '../index.php';

// Start class
$crawler = new WronnaySearchLib\Crawler();

// Get links of my website
print_r($crawler->getLinks('http://christoph.miksche.org'));
