#1 May 2016 Graduation Project 2016
#Features Matrix Extractor
#Nora Basha , Aliaa Alzohairy , Ahmed Al-Badrawy
#############################
#Importing necessary libraries
import numpy as np
import cv2
import datetime
from datetime import date
from json import dumps
def gettype():
    im = cv2.imread('7.jpg')# Enter Image Path
    imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    im1 = cv2.equalizeHist(imgray)
    edges = cv2.Canny(im1,127,255)
    k=cv2.getStructuringElement(cv2.MORPH_RECT,(10,10))
    closed=cv2.morphologyEx(edges, cv2.MORPH_CLOSE, k)
    image, cnts, hierarchy = cv2.findContours(closed,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]
    count= len(cnts)
    peri = np.zeros(count)
    for c in range(0,count):
            # approximate the contour
        contour=cnts[c]
        peri[c] = cv2.arcLength(contour, True)          
    cntindex=np.argmax(peri)
    cnt= cnts[cntindex]
    x=np.zeros(42)
    b,g,r = cv2.split(im)
    mask = np.zeros_like(imgray)
    cv2.drawContours(mask, [cnt], 0, 255, -1)
    outb = np.zeros_like(imgray)
    outb[mask == 255] = b[mask == 255]
    outg = np.zeros_like(imgray)
    outg[mask == 255] = g[mask == 255]
    outr = np.zeros_like(imgray)
    outr[mask == 255] = r[mask == 255]
    out= cv2.merge([outb, outg, outr])
    (hight,width)=out.shape[:2]
    # Numbers of rows
    nRows = 2
    n=3
    # Number of columns
    mCols = 2
    m=3
    # Tam of Y region
    regionY=hight/nRows
    # Tam of X region 
    regionX = width/mCols
    # Total of regions
    totalRegions = nRows* mCols
    t=totalRegions+1

    for i in range(1,3):
              for j in range(1,3):
                            part=out[(i-1)*regionX:i*regionX,
                                   (j-1)*regionY:j*regionY]
                            
                            cv2.imwrite(str(i)+str(j)+'.jpg',part)
                            
    #Extracting features
    x[0]=cv2.contourArea(cnt)
    x[1]=cv2.arcLength(cnt,True)
    piece11=cv2.imread('11.jpg')
    blue,green,red=cv2.split(piece11)
    x[2]=np.average(blue)
    x[3]=np.average(green)
    x[4]=np.average(red)
    x[5]=np.var(blue)
    x[6]=np.var(green)
    x[7]=np.var(red)
    (a1,b1)=piece11.shape[:2]
    rgb111 = piece11[a1/2+20,b1/2+10]
    x[8]= rgb111[0]+rgb111[1]*256+rgb111[2]*256*256
    rgb112 = piece11[a1/2+6,b1/2+2]
    x[9]=rgb112[0]+rgb112[1]*256+rgb112[2]*256*256
    rgb113 = piece11[a1/2+11,b1/2+1]
    x[10]=rgb113[0]+rgb113[1]*256+rgb113[2]*256*256
    rgb114 = piece11[a1/2+20,b1/2+2]
    x[11]=rgb114[0]+rgb114[1]*256+rgb114[2]*256*256
    ###############################################
    piece12=cv2.imread('12.jpg')
    blue,green,red=cv2.split(piece12)
    x[12]=np.average(blue)
    x[13]=np.average(green)
    x[14]=np.average(red)
    x[15]=np.var(blue)
    x[16]=np.var(green)
    x[17]=np.var(red)
    (a2,b2)=piece12.shape[:2]
    rgb121 = piece12[a2/2,b2/2]
    x[18]=rgb121[0]+rgb121[1]*256+rgb121[2]*256*256
    rgb122 = piece12[a2/2+1,b2/2+10]
    x[19]=rgb122[0]+rgb122[1]*256+rgb122[2]*256*256
    rgb123 = piece12[a2/2+5,b2/2+6]
    x[20]=rgb123[0]+rgb123[1]*256+rgb123[2]*256*256
    rgb124 = piece12[a2/2+10,b2/2]
    x[21]=rgb124[0]+rgb124[1]*256+rgb124[2]*256*256
    ##############################################
    piece21=cv2.imread('21.jpg')
    blue,green,red=cv2.split(piece21)
    x[22]=np.average(blue)
    x[23]=np.average(green)
    x[24]=np.average(red)
    x[25]=np.var(blue)
    x[26]=np.var(green)
    x[27]=np.var(red)
    (a3,b3)=piece21.shape[:2]
    rgb211 = piece21[a3/2,b3/2]
    x[28]= rgb211[0]+rgb211[1]*256+rgb211[2]*256*256
    rgb212 = piece21[a3/2+10,b3/2+4]
    x[29]= rgb212[0]+rgb212[1]*256+rgb212[2]*256*256
    rgb213 = piece21[a3/2+6,b3/2+3]
    x[30]= rgb213[0]+rgb213[1]*256+rgb213[2]*256*256
    rgb214 = piece21[a3/2+9,b3/2+7]
    x[31]= rgb214[0]+rgb214[1]*256+rgb214[2]*256*256
    ###############################################
    piece22=cv2.imread('22.jpg')
    blue,green,red=cv2.split(piece22)
    x[32]=np.average(blue)
    x[33]=np.average(green)
    x[34]=np.average(red)
    x[35]=np.var(blue)
    x[36]=np.var(green)
    x[37]=np.var(red)
    (a4,b4)=piece22.shape[:2]
    rgb221 = piece22[a4/2,b4/2]
    x[38]= rgb221[0]+rgb221[1]*256+rgb221[2]*256*256
    rgb222 = piece22[a4/2+6,b4/2+6]
    x[39]= rgb222[0]+rgb222[1]*256+rgb222[2]*256*256
    rgb223 = piece22[a4/2+10,b4/2]
    x[40]= rgb223[0]+rgb223[1]*256+rgb223[2]*256*256
    rgb224 = piece22[a4/2+9,b4/2+10]
    x[41]= rgb224[0]+rgb224[1]*256+rgb224[2]*256*256

    import json, ast
    import urllib2
    # If you are using Python 3+, import urllib instead of urllib2

    x.tolist()
    data =  {

            "Inputs": {

                    "input1":
                    {
                        "ColumnNames": ["Contour length", "Contour area", "mean blue1", "mean green1", "mean red1", "varb1", "varg1", "varr1", "pix11", "pix21", "pix31", "pix41", "mean blue2", "mean green2", "mean red2", "varb2", "varg2", "varr2", "pix12", "pix22", "pix32", "pix42", "mean blue3", "mean green3", "mean red3", "varb3", "varg3", "varr3", "pix13", "pix23", "pix33", "pix43", "mean blue4", "mean green4", "mean red4", "varb4", "varg4", "varr4", "pix14", "pix24", "pix34", "pix44"],
                        "Values": [[x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8],x[9],x[10],x[11],x[12],x[13],x[14],x[15],x[16],x[17],x[18],x[19],x[20],x[21],x[22],x[23],x[24],x[25],x[26],x[27],x[28],x[29],x[30],x[31],x[32],x[33],x[34],x[35],x[36],x[37],x[38],x[39],x[40],x[41]]],
                    },        },
                "GlobalParameters": {
    }
        }


        
                    
    #cv2.imshow('gray scale', imgray)
    #cv2.imshow('Original', im)
    #cv2.imshow('Edges',edges)
    #cv2.imshow('Morphological closing', closed)
    #cv2.imshow('Mask',mask)
    #cv2.imshow('outb',outb)
    #cv2.imshow('outg',outg)
    #cv2.imshow('out',out)
    #cv2.imshow('enhanced',im1)
    cv2.waitKey(0)
    return data
