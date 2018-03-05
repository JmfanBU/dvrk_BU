/* -*- Mode: C++; tab-width: 4; indent-tabs-mode: nil; c-basic-offset: 4 -*-    */
/* ex: set filetype=cpp softtabstop=4 shiftwidth=4 tabstop=4 cindent expandtab: */

/*
  Author(s):  Anton Deguet
  Created on: 2016-02-24

  (C) Copyright 2013-2017 Johns Hopkins University (JHU), All Rights Reserved.

--- begin cisst license - do not edit ---

This software is provided "as is" under an open source license, with
no warranty.  The complete license can be found in license.txt and
http://www.cisst.org/cisst/license.txt.

--- end cisst license ---
*/

#ifndef _mtsIntuitiveResearchKit_h
#define _mtsIntuitiveResearchKit_h

#include <sawIntuitiveResearchKit/sawIntuitiveResearchKitExport.h>

namespace mtsIntuitiveResearchKit {
    const double IOPeriod = 0.3 * cmn_ms;
    const double ArmPeriod = 0.5 * cmn_ms;
    const double TeleopPeriod = 1.0 * cmn_ms;
    const double WatchdogTimeout = 30.0 * cmn_ms;
    const double TimeToPower = 5.0 * cmn_s;
};

#endif // _mtsIntuitiveResearchKitArm_h
