// file automatically generated, do not modify
// cisst version: 1.0.9
// source file: /home/jiameng/catkin_dvrk/src/cisst-saw/sawConstraintController/components/code/prmForceOffsetState.cdg

#pragma once
#ifndef _sawConstraintController_prmForceOffsetState_h
#define _sawConstraintController_prmForceOffsetState_h

#include <cisstCommon/cmnDataFunctions.h>
#include <cisstCommon/cmnDataFunctionsEnumMacros.h>
#if CISST_HAS_JSON
#include <cisstCommon/cmnDataFunctionsJSON.h>
#endif // CISST_HAS_JSON

/* source line: 1 */

/* source line: 9 */

// mts-proxy set to true
#include <cisstCommon/cmnClassServices.h>
#include <cisstCommon/cmnClassRegisterMacros.h>
#include <cisstMultiTask/mtsGenericObjectProxy.h>



/* source line: 1 */
/* source line: 1 */

#include <cisstCommon/cmnGenericObject.h> 
#include <cisstVector/vctDynamicVectorTypes.h>
#include <cisstVector/vctFixedSizeVectorTypes.h>
#include <cisstVector/vctDynamicMatrixTypes.h>
#include <cisstVector/vctFixedSizeVectorTypes.h>
#include <sawConstraintController/prmOffsetState.h>

/* source line: 9 */
class  prmForceOffsetState: public prmOffsetState
{
 /* default constructors and destructors. */
 public:
    prmForceOffsetState(void);
    prmForceOffsetState(const prmForceOffsetState & other);
    ~prmForceOffsetState();

/* source line: 16 */

        /*! Constructor
        */
        prmForceOffsetState(const std::string & n, const std::string & bn, const vctFrm3 & of) : prmOffsetState(n,bn,of){}

        //! Updates values based on those of the base force sensor
        /*! Update
        */
        void Update();
        /* default methods */
 public:
    void SerializeRaw(std::ostream & outputStream) const;
    void DeSerializeRaw(std::istream & inputStream);
    void ToStream(std::ostream & outputStream) const;
    void ToStreamRaw(std::ostream & outputStream, const char delimiter = ' ',
                     bool headerOnly = false, const std::string & headerPrefix = "") const;
    /* default data methods */
 public:
    void Copy(const prmForceOffsetState & source);
    void SerializeBinary(std::ostream & outputStream) const throw (std::runtime_error);
    void DeSerializeBinary(std::istream & inputStream, const cmnDataFormat & localFormat, const cmnDataFormat & remoteFormat) throw (std::runtime_error);
    void SerializeText(std::ostream & outputStream, const char delimiter = ',') const throw (std::runtime_error);
    std::string SerializeDescription(const char delimiter = ',', const std::string & userDescription = "") const;
    void DeSerializeText(std::istream & inputStream, const char delimiter = ',') throw (std::runtime_error);
    std::string HumanReadable(void) const;
    bool ScalarNumberIsFixed(void) const;
    size_t ScalarNumber(void) const;
    double Scalar(const size_t index) const throw (std::out_of_range);
    std::string ScalarDescription(const size_t index, const std::string & userDescription = "") const throw (std::out_of_range);
#if CISST_HAS_JSON
    void SerializeTextJSON(Json::Value & jsonValue) const;
    void DeSerializeTextJSON(const Json::Value & jsonValue) throw (std::runtime_error);
#endif // CISST_HAS_JSON

}; // prmForceOffsetState

// mts-proxy set to true
typedef mtsGenericObjectProxy<prmForceOffsetState> prmForceOffsetStateProxy;
CMN_DECLARE_SERVICES_INSTANTIATION(prmForceOffsetStateProxy);

/* default functions */
void  cmnSerializeRaw(std::ostream & outputStream, const prmForceOffsetState & object);
void  cmnDeSerializeRaw(std::istream & inputStream, prmForceOffsetState & placeHolder);
/* data functions */
template <> class cmnData<prmForceOffsetState > {
public: 
    enum {IS_SPECIALIZED = 1};
    typedef prmForceOffsetState DataType;
    static void Copy(DataType & data, const DataType & source) {
        data.Copy(source);
    }
    static std::string SerializeDescription(const DataType & data, const char delimiter, const std::string & userDescription) {
        return data.SerializeDescription(delimiter, userDescription);
    }
    static void SerializeBinary(const DataType & data, std::ostream & outputStream) throw (std::runtime_error) {
        data.SerializeBinary(outputStream);
    }
    static void DeSerializeBinary(DataType & data, std::istream & inputStream, const cmnDataFormat & localFormat, const cmnDataFormat & remoteFormat) throw (std::runtime_error) {
        data.DeSerializeBinary(inputStream, localFormat, remoteFormat);
    }
    static void SerializeText(const DataType & data, std::ostream & outputStream, const char delimiter = ',') throw (std::runtime_error) {
        data.SerializeText(outputStream, delimiter);
    }
    static void DeSerializeText(DataType & data, std::istream & inputStream, const char delimiter = ',') throw (std::runtime_error) {
        data.DeSerializeText(inputStream, delimiter);
    }
    static std::string HumanReadable(const DataType & data) {
        return data.HumanReadable();
    }
    static bool ScalarNumberIsFixed(const DataType & data) {
        return data.ScalarNumberIsFixed();
    }
    static size_t ScalarNumber(const DataType & data) {
        return data.ScalarNumber();
    }
    static std::string ScalarDescription(const DataType & data, const size_t index, const std::string & userDescription = "") throw (std::out_of_range) {
        return data.ScalarDescription(index, userDescription);
    }
    static double Scalar(const DataType & data, const size_t index) throw (std::out_of_range) {
        return data.Scalar(index);
    }
};
inline std::ostream & operator << (std::ostream & outputStream, const prmForceOffsetState & data) {
    outputStream << cmnData<prmForceOffsetState >::HumanReadable(data);
    return outputStream;
}
#if CISST_HAS_JSON
template <> void  cmnDataJSON<prmForceOffsetState >::SerializeText(const prmForceOffsetState & data, Json::Value & jsonValue);
template <> void  cmnDataJSON<prmForceOffsetState >::DeSerializeText(prmForceOffsetState & data, const Json::Value & jsonValue) throw (std::runtime_error);
#endif // CISST_HAS_JSON



#endif // _sawConstraintController_prmForceOffsetState_h
