//
//  ViewController.swift
//  JPHACKS_smp
//  Sample iOS app
//
//  Created by bashow on 2017/07/13.
//  Copyright © 2017年 bashow. All rights reserved.
//

import UIKit
import GoogleMaps


class ViewController: UIViewController {
    
    // You don't need to modify the default init(nibName:bundle:) method.
    
    override func loadView() {
        // Create a GMSCameraPosition that tells the map to display the
        // coordinate -33.86,151.20 at zoom leve    l 6.

        
        let camera = GMSCameraPosition.camera(withLatitude: 35.7126781, longitude: 139.7584809, zoom: 15.0)
        let mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
        mapView.isMyLocationEnabled = true
        view = mapView
        
        // Creates a marker in the center of the map.
        /*
         35.7126781,139.7584809
        let marker = GMSMarker()
         marker.position = CLLocationCoordinate2D(latitude: 36.25, longitude: 136.35)
         marker.title = "Jaist"
         marker.snippet = "Japan"
         marker.map = mapView
        */
        
        let pathURL = NSURL(string: "AWS Server address")
        var csvString = ""
        
        do {
            csvString = try NSString(contentsOf: pathURL as! URL, encoding: String.Encoding.utf8.rawValue) as String
        } catch let error as NSError {
            print(error.localizedDescription)
        }

        csvString.enumerateLines { (line, stop) -> () in
            let bearData = line.components(separatedBy: ",")
            let position = CLLocationCoordinate2D(latitude: atof(bearData[2]), longitude: atof(bearData[3]))
            let marker = GMSMarker(position: position)
            marker.title = bearData[0]
            marker.snippet = bearData[1]
            marker.map = mapView

        }

        
    }

    
}

